from datetime import date, timedelta
import requests
import pandas as pd

def get_meteo_passe(longitude, latitude, date_debut, date_fin):
    """
    (longitude, latitude, date_debut, date_fin) -> DataFrame
    indexé par date, colonnes : temperature_2m_max, temperature_2m_min,
    precipitation_sum.
    """
    r = requests.get(
        "https://archive-api.open-meteo.com/v1/archive",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "start_date": date_debut,
            "end_date": date_fin,
            "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
            "timezone": "Europe/Paris",
        },
    )
    r.raise_for_status()
    df = pd.DataFrame(r.json()["daily"])
    df["time"] = pd.to_datetime(df["time"])
    return df.set_index("time").rename_axis("date")

MODELES_CMIP6 = [
    "CMCC_CM2_VHR4", "FGOALS_f3_H", "HiRAM_SIT_HR",
    "MRI_AGCM3_2_S", "EC_Earth3P_HR", "MPI_ESM1_2_XR", "NICAM16_8S",
]

BORNE_MAX_PROJETE = date(2050, 12, 31)

def get_meteo_projete(longitude, latitude, date_debut, date_fin, modele="CMCC_CM2_VHR4"):
    """
    Comme get_meteo_projete, mais pour un seul modèle CMIP6 -> sortie
    homogène avec get_meteo (une ligne par date, pas de colonne 'modele').
    """
    debut = pd.Timestamp(date_debut).date()
    fin = min(pd.Timestamp(date_fin).date(), BORNE_MAX_PROJETE)
    if debut > fin:
        raise ValueError(f"Plage hors couverture du Climate API (jusqu'à {BORNE_MAX_PROJETE}).")

    r = requests.get(
        "https://climate-api.open-meteo.com/v1/climate",
        params={
            "latitude": latitude, "longitude": longitude,
            "start_date": debut.isoformat(), "end_date": fin.isoformat(),
            "models": [modele],
            "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
            "timezone": "Europe/Paris",
        },
    )
    r.raise_for_status()
    daily = r.json()["daily"]
    dates = pd.to_datetime(daily["time"])

    data = {}
    for var in ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"]:
        cle = f"{var}_{modele}" if f"{var}_{modele}" in daily else var
        data[var] = daily[cle]

    return pd.DataFrame(data, index=dates).rename_axis("date")

def get_meteo(longitude, latitude, date_debut, date_fin,
                   modele="CMCC_CM2_VHR4", aujourdhui=None):
    """
    (longitude, latitude, date_debut, date_fin) -> DataFrame homogène
    (temperature_2m_max, temperature_2m_min, precipitation_sum),
    quelle que soit la date : ERA5 pour le passé (get_meteo),
    un seul modèle CMIP6 pour le futur (get_meteo_projete_unique).
    """
    aujourdhui = aujourdhui or date.today()
    debut = pd.Timestamp(date_debut).date()
    fin = pd.Timestamp(date_fin).date()

    morceaux = []

    if debut <= aujourdhui:
        fin_obs = min(fin, aujourdhui)
        morceaux.append(get_meteo_passe(longitude, latitude, debut.isoformat(), fin_obs.isoformat()))

    if fin > aujourdhui:
        debut_proj = max(debut, aujourdhui + timedelta(days=1))
        morceaux.append(get_meteo_projete(longitude, latitude,
                                                   debut_proj.isoformat(), fin.isoformat(), modele))

    if not morceaux:
        raise ValueError("Plage de dates vide.")

    return pd.concat(morceaux).sort_index()

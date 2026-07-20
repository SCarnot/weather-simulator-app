from meteo_app.get_meteo import get_meteo

df = get_meteo(
    longitude=2.35,        # Paris, à titre d'exemple
    latitude=48.85,
    date_debut="2023-01-01",
    date_fin="2023-01-05")

print(df.head())
print(df.dtypes)
print(df.shape)

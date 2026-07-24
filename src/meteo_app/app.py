from flask import Flask, render_template, request
from meteo_app.geocodage import get_coordinates
from meteo_app.get_meteo import get_meteo

MODELE_PAR_DEFAUT = "CMCC_CM2_VHR4"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/resultats", methods=["POST"])
def resultats():
    lieu = request.form["lieu"]
    date_debut = request.form["date_debut"]
    date_fin = request.form["date_fin"]

    try:
        latitude, longitude = get_coordinates(lieu)
    except ValueError as e:
        return str(e)

    df = get_meteo(longitude, latitude, date_debut, date_fin, MODELE_PAR_DEFAUT)

    return df.to_html()

if __name__ == "__main__":
    app.run(debug=True)

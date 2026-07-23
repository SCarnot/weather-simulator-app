# Weather Simulator App

EN : Will the weather be like in your city in July 2046 or December 2049? Simulate the weather in your city in the near future by visualizing, day by day, weather (temperatures, precipitation) that would be plausible in the context of climate change. This application aims to help users get a concrete sense of what a weather sequence (for example, a summer in the 2040s decade) could look like in a specific location. For instance, it makes it possible to assess, in an agricultural context, the viability of growing a given crop in a given place, by estimating yields over several consecutive years.

/!\ This is not a weather forecast, but a simulation: the application proposes weather sequences that are PLAUSIBLE in the context of climate change, but it does not predict the exact weather on a specific date. /!\


FR : Quelle sera la météo dans votre ville en juillet 2046 ou en décembre 2049 ? Simulez la météo dans votre ville dans un. futur proche, en visualisant jour par jour une météo (températures, précipitations) qui sera plausible dans le contexte du réchauffement climatique. Cette application a pour but de permettre aux utilisateurs de se rendre compte concrètement à quoi pourrait ressembler une séquence météo (par exemple un été dans la décénnie 2040) dans un lieu précis. Par exemple, il est posible d'évaluer en agriculture la viabilité d'une culture à un endroit donné, en estimant les rendements sur plusieurs années successives.

/!\ Ce n'est pas une prévision météo, mais une simulation : l'application propose des séquences météo PROBABLES dans le contexte du réchauffmeenbt climatique, mais pas prévoir le temps exact qu'il fera à une date précise. /!\

## Features/Fonctionnalités

EN : Like a typical weather app, simply enter the location where you want to simulate the weather, then choose a date range to visualize the main weather characteristics (minimum temperature, maximum temperature, precipitation, etc.). The time selection works both for the past (real observations) and for the future (simulation based on weather and climate models).

/!\ under construction /!\

FR : Comme une application météo classique, il suffit de rentrer le lieu où vous souhaitez simulez le temps qu'il fera, puis de choisir une plage de dates pour visualiser les principales caractéristiques météorologiques (température minimale, température maximale, précipitations, etc.). Le choix temporel se fait aussi bien pour le passé (observations réelles) que dans le futur (simulation à partir de modèles météorologiques et climatiques).

/!\ en contruction /!\

## Structure du projet

weather-simulator-app/
|-- src/
|   |-- meteo_app/
|       |-- init.py
|       |-- get_meteo.py      # Fonction principale de récupération météo
|-- notebooks/
|   |-- test_manuel.py        # Script de test manuel
|-- requirements.txt          # Dépendances Python
|-- pyproject.toml            # Configuration du package
|-- README.md

## Installation

1. Cloner le dépôt :
```bash
   git clone git@github.com:SCarnot/weather-simulator-app.git
   cd weather-simulator-app
```

2. Créer et activer l'environnement virtuel :
```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. Installer les dépendances et le projet en mode éditable :
```bash
   pip install -r requirements.txt
   pip install -e .
```
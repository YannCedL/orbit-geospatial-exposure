# API FastAPI pour le moteur Orbit Geospatial Exposure
import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from genesis_core import ResultContract
from .risk import calculate_site_risk

app = FastAPI(
    title="Orbit Geospatial Exposure API",
    description="Moteur de Calcul d'Exposition aux Risques Géospatiaux",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert la page d'accueil avec carte d'exposition
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Orbit API - Interface non trouvee</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Orbit", "version": "1.0.0"}

@app.get("/api/v1/risk", response_model=ResultContract)
def get_risk(lat: float = Query(48.8566), lon: float = Query(2.3522)):
    return calculate_site_risk(lat, lon)

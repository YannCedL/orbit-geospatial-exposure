# test du calcul de risque géospatial Orbit
from orbit_geospatial_exposure.risk import calculate_site_risk

def test_calculate_site_risk():
    contract = calculate_site_risk(48.8566, 2.3522)
    assert contract is not None
    assert contract.result["overall_risk_score"] > 0
    assert len(contract.evidence) >= 1

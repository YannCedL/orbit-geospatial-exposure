from orbit_geospatial_exposure import calculate_site_risk

def test_calculate_site_risk():
    c = calculate_site_risk(43.6047, 1.4442)
    assert "flood_risk" in c.result
    assert c.result["overall_risk"] >= 0

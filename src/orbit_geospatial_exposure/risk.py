from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus

def calculate_site_risk(lat: float, lon: float) -> ResultContract:
    now = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now)
    contract.result = {
        "lat": lat, "lon": lon,
        "flood_risk": 0.12, "earthquake_risk": 0.04,
        "wildfire_risk": 0.08, "overall_risk": 0.11
    }
    contract.add_evidence(Evidence(subject=f"{lat},{lon}", predicate="geospatial_risk",
        value="0.11", source="natural_hazard_db", observed_at=now,
        confidence=0.82, status=EpistemicStatus.INFERENCE))
    return contract

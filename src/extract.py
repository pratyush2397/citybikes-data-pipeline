import json
from datetime import datetime
from pathlib import Path

from src.client import CityBikesClient

RAW_DATA_DIR = Path("data_raw")

def save_raw_json(data: dict,prefix: str) -> None:
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filename = RAW_DATA_DIR/f"{prefix}_{timestamp}.json"

    with open(filename, "w",encoding="utf-8") as f:
        json.dump(data,f,indent=2)
    print(f"Saved Raw data to {filename}")

def extract_network(network_id: str) -> dict:
    client = CityBikesClient()
    data = client.get_network_data(network_id)
    save_raw_json(data,network_id)
    return data
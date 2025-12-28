import numpy as np
import os
from src.schema import (NETWORK_FIELDS,STATION_METADATA_FIELDS,STATION_STATUS_FIELDS)
from datetime import datetime

def transform_network_data(raw_json:dict):
    network = raw_json["network"]

    row = [
        network.get("id"),
        network.get("name"),
        network.get("location",{}).get("city"),
        network.get("location",{}).get("country"),
    ]

    return np.array([row],dtype=object)

def transform_station_data(raw_json:dict):
    stations = raw_json["network"]["stations"]
    metadata_rows = []
    status_rows = []

    for station in stations:
        extra = station.get("extra",{})

        metadata_rows.append([
            station.get("id"),
            extra.get("uid"),
            station.get("name"),
            station.get("latitude"),
            station.get("longitude"),
            extra.get("address"),
            extra.get("slots"),
            extra.get("payment-terminal"),
            extra.get("virtual"),
        ])

        status_rows.append([
            station.get("id"),
            station.get("free_bikes"),
            station.get("empty_slots"),
            extra.get("renting"),
            extra.get("returning"),
            station.get("timestamp"),
            extra.get("last_updated"),
        ])

    metadata_array = np.array(metadata_rows,dtype=object)
    status_array = np.array(status_rows,dtype=object)

    return metadata_array,status_array

def save_table(array,headers,name,network_id):
    os.makedirs("data_processed",exist_ok = True)
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    path = f"data_processed/{network_id}_{name}_{ts}.csv"
    header = ",".join(headers)

    np.savetxt(path,array,delimiter=",",fmt = "%s",header=header,comments="")

    print(f"Saved {name} to {path}")
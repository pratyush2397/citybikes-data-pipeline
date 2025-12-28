from src.extract import extract_network
from src.transform import (transform_network_data,transform_station_data,save_table)
from src.schema import (NETWORK_FIELDS,STATION_METADATA_FIELDS,STATION_STATUS_FIELDS,)



def run():
    network_id = "abu-dhabi-careem-bike"

    raw = extract_network(network_id)

    network_table = transform_network_data(raw)
    station_meta, station_status = transform_station_data(raw)

    save_table(network_table, NETWORK_FIELDS, "network_metadata",network_id)
    save_table(station_meta, STATION_METADATA_FIELDS, "station_metadata",network_id)
    save_table(station_status, STATION_STATUS_FIELDS, "station_status",network_id)

if __name__ == "__main__":
    run()
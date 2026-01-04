import os
import numpy as np
import matplotlib.pyplot as plt

def _latest_file(prefix):
    files = [f for f in os.listdir("data_processed") if f.startswith(prefix)]
    if not files:
        raise FileNotFoundError("No Processed files found. Run pipeline first.")
    files.sort(reverse=True)

    return os.path.join("data_processed", files[0])

def plot_station_availability(network_id):

    os.makedirs("plots", exist_ok=True)
    path = _latest_file(f"{network_id}_station_status")
    data = np.genfromtxt(path, delimiter = ",", skip_header=1,dtype=object)
    free_bikes = data[:,1].astype(int)
    empty_slots = data[:,2].astype(int)

    x = np.arange(len(free_bikes))

    plt.figure(figsize=(14,6))
    plt.bar(x, free_bikes, label = "Free Bikes")
    plt.bar(x,empty_slots,bottom=free_bikes,label= "Empty Slots")
    plt.title("Bike Availability by Station")
    plt.xlabel("Station Index")
    plt.ylabel("Count")
    plt.legend()

    output = f"plots/{network_id}_availability.png"
    plt.tight_layout()
    plt.savefig(output)
    plt.close()

    print(f"Saved Plot {output}")

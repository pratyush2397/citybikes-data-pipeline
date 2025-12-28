import requests
from typing import Dict

class CityBikesClient:
    """Client to interact with the citybikes Public API"""

    BASE_URL = "https://api.citybik.es/v2"

    def get_all_networks(self) -> Dict:

        url = f"{self.BASE_URL}/networks"
        response = requests.get(url,timeout=10)
        response.raise_for_status()

        return response.json()
    
    def get_network_data(self, network_id: str) -> Dict:

        url = f"{self.BASE_URL}/networks/{network_id}"
        response = requests.get(url,timeout=10)
        response.raise_for_status()

        return response.json()
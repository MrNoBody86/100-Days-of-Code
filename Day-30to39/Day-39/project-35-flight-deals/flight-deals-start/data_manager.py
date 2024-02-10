"""This class is responsible for talking to the Google Sheet."""

import requests

class DataManager:
    def __init__(self) -> None:
        self.url = "https://api.sheety.co/407bd5b3fc8ff807ff0ce54e08b178fd/flightDeals/prices"
        self.response = requests.get(url=self.url,timeout=None)
        self.json = self.response.json()
        count = 0
        # for row in self.json["prices"]:
        #     count += 1
        #     if row["iataCode"] == "":
        
        row_update = {
            "prices":{
                    "iataCode" : "Testing"
                }
                }
                
        requests.put(url=f"{self.url}/2",timeout=None,json=row_update)

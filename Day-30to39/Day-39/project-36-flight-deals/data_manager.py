"""This class is responsible for talking to the Google Sheet."""

import requests

class DataManager:
    def __init__(self) -> None:
        self.url = YOUR SHEETY PRICES ENDPOINT
        self.response = requests.get(url=self.url,timeout=None)
        self.json = self.response.json()
        
    def updateiata(self,row):
        row_update = {
            "price":{
                    "iataCode" : f"{row['iataCode']}"
                }
                }
        response = requests.put(url=f"{self.url}/{row['id']}",json=row_update,timeout=None)
        print(response.text)

    def updateprice(self,row,flight):
        row_update = {
            "price":{
                "lowestPrice" : f"{flight.price}"
            }
        }
        response = requests.put(url=f"{self.url}/{row['id']}",json=row_update,timeout=None)
        print(response.text)

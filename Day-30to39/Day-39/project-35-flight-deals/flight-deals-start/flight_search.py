"""This class is responsible for talking to the Flight Search API."""
import os
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

class FlightSearch:
    def __init__(self,fly_from,fly_to) -> None:
        self.six_months = datetime.now() + relativedelta(months=+6)
        self.tomorrow = datetime.today() + relativedelta(days=+1)
        self.url = "https://api.tequila.kiwi.com/v2/search"
        self.header = {
            "accept" : "application/json",
            "apikey" : os.environ.get("tequila_api"),
        }
        self.params = {
            
            "fly_from" : fly_from,
            "fly_to" : fly_to,
            "date_from" : self.tomorrow.strftime("%d/%m/%Y"),
            "date_to" : self.six_months.strftime("%d/%m/%Y"),
            "sort" : "price",
            "limit" : "1",
        }
        self.response = requests.get(url=self.url,timeout=None,headers=self.header,params=self.params)
        self.response.raise_for_status()
        self.json = self.response.json()

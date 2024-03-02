"""This class is responsible for talking to the Flight Search API."""
import os
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
from flight_data import FlightData

DATE_FORMAT = "%d/%m/%Y"

class FlightSearch:
    def __init__(self) -> None:
        self.fly_from = "LON"
        self.six_months = datetime.now() + relativedelta(months=+6)
        self.tomorrow = datetime.today() + relativedelta(days=+1)
        self.week = datetime.today() + relativedelta(days=+7)
        self.month = datetime.today() + relativedelta(days=+30)
        self.url = "https://api.tequila.kiwi.com/"
        self.header = {
            "accept" : "application/json",
            "apikey" :YOUR FLIGHT SEARCH API KEY,
        }
        self.response = None
        self.params = None
        self.json = None

    def getiata(self,city):
        params = {
            "term" : city,
            "location_types" : "city"
        }
        response = requests.get(url=f'{self.url}locations/query',
                                timeout=None,
                                headers=self.header,
                                params=params)
        response.raise_for_status()
        json = response.json()
        code = json["locations"][0]["code"]
        return code
    
    def getcheapflights(self,code):
        self.params = {
            "fly_from" : self.fly_from,
            "fly_to" : code,
            "date_from" : self.tomorrow.strftime(DATE_FORMAT),
            "date_to" : self.six_months.strftime(DATE_FORMAT),
            "return_from" : self.week.strftime(DATE_FORMAT),
            "return_to" : self.month.strftime(DATE_FORMAT),
            "sort" : "price",
            "limit" : "1",
            "curr" : "GBP",
        }
        self.response = requests.get(url=f'{self.url}v2/search',
                                     timeout=None,
                                     headers=self.header,
                                     params=self.params)
        self.response.raise_for_status()
        try:
            data = self.response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        
        return flight_data

"""This file will need to use the DataManager,FlightSearch, FlightData, 
NotificationManager classes to achieve the program requirements."""
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

FLY_FROM = "BOM"
FLY_TO = "NYC"

sheet_data = DataManager()
search = FlightSearch(FLY_FROM,FLY_TO)

pprint(sheet_data.json)
pprint(search.json["data"][0]["price"])

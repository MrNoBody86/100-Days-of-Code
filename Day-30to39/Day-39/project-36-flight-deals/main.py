"""This file will need to use the DataManager,FlightSearch, FlightData, 
NotificationManager classes to achieve the program requirements."""

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


data = DataManager()
sheet_data = data.json["prices"]

search = FlightSearch()

for row in sheet_data:
    if row["iataCode"] == "":
        iatacode = search.getiata(row["city"])
        row["iataCode"] = iatacode
        data.updateiata(row)
    else:
        flight = search.getcheapflights(row["iataCode"])
        print(f"{flight.destination_city}: £{flight.price}")
        if int(flight.price) < int(row["lowestPrice"]) :
            data.updateprice(row,flight)
            msg = NotificationManager()
            body = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport} from {flight.out_date} to {flight.return_date}."
            msg.send_sms(body)

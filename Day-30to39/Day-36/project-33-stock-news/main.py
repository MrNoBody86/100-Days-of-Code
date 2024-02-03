import os
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = os.environ.get("ALPHA_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
CLOSE = "4. close"

twilio_account_sid = os.environ.get("twilio_account_sid")
twilio_auth_token = os.environ.get("twilio_auth_token")

mgs_percent = None

alpha_parameter = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : ALPHA_API_KEY,
}

news_parameter = {
    "qInTitle" : COMPANY_NAME,
    "sortBy" : "popularity",
    "apiKey" : NEWS_API_KEY,
    "pageSize" : 10,
    "page" : 1,
    "language" : "en",
}


alpha_response = requests.get(url="https://www.alphavantage.co/query",
                              timeout=None,params= alpha_parameter)
alpha_response.raise_for_status()

stock_data = [value for (_,value)  in alpha_response.json()['Time Series (Daily)'].items()]

yesterday = float(stock_data[0][CLOSE])
day_before_yesterday = float(stock_data[1][CLOSE])
diff  = (yesterday - day_before_yesterday)*100/day_before_yesterday

if diff > 0 :
    mgs_percent = f"🔺{diff}%"
else:
    mgs_percent = f"🔻{diff}%"

if abs(diff) > 5 :
    news_response = requests.get(url="https://newsapi.org/v2/everything",
                                 timeout=None,
                                 params=news_parameter)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][2:5]
    for news in news_data:
        client = Client(twilio_account_sid, twilio_auth_token)
        message = client.messages \
                    .create(
                        body=f"\n{STOCK}: {mgs_percent}\nHeadline: {news['title']}\nBrief: {news['description']}",
                        from_='+19254063531',
                        to='+919970106137'
                    )
        print(message.status)

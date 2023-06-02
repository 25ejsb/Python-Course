STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "C6NZ7EVG6LRHFT5J"

NEWS_API_KEY = "8d4bf082283441bb83ce26e0e2b48fac"

# use https://jsonviewer.stack.hu

STACK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

twillio_api_key = "02d5313f254a2c3a43eb6e398fb5c9a7"
account_sid = "AC867126c1cc6df9793345f8aecccb2852"
auth_token = "059d9391c2eb4f8e313bbaf31d04c26d"

import requests
from twilio.rest import Client

params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": API_KEY
}

response = requests.get(STACK_ENDPOINT, params=params)
response.raise_for_status()
json = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in json.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday = data_list[1]
day_closing_price = day_before_yesterday["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_closing_price))

diff_percent = (difference / float(yesterday_closing_price)) * 100

# Messages are too long, that's why I can't send news

if diff_percent > 5:
    news_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = ["Headline: " + article["title"] for article in three_articles]
    for i in formatted_articles:
        print(i)
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"{STOCK} has just received a huge change! Read the news!",
        from_='+18884017099',
        to='7812289821'
    )
    print(message.status)
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
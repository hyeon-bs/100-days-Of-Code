import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = "*"
NEWS_API = "*"

account_sid = "*"
auth_token = "*"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

difference_percent = (difference / float(yesterday_closing_price)) * 100
print(difference_percent)

if difference_percent > 1:
    news_params = {
        "q": STOCK,
        "apikey": NEWS_API,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"Healine: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body = article,
            from_ = "whatsapp:+*",
            to = "whatsapp:+*",
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


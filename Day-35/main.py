import requests, os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "*"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 35.689487,
    "lon": 139.691711,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

# for hour_data in weather_slice:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) <= 700:
#         print("Bring an Umbrella. ☔️")
#         break

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = "It's going to rain today. Remember to bring an ☔️",
        from_='whatsapp:+*',
        to='whatsapp:+*',
    )
    print(message.status)

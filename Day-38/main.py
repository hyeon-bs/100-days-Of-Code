import requests
from datetime import datetime

GENDER = "Female"
WEIGHT_KG = "65"
HEIGHT_CM = "170"
AGE = "25"

API_ID = "*"
API_KEYS = "*"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/e242f53c7084cf4a1b07b82924939b7f/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEYS,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)

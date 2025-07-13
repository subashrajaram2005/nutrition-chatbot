import requests
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")

def get_nutrition(food_item):
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "Content-Type": "application/json"
    }
    data = {"query": food_item}
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        food = response.json()['foods'][0]
        return {
            "name": food["food_name"],
            "calories": food["nf_calories"],
            "protein": food["nf_protein"],
            "fat": food["nf_total_fat"],
            "carbs": food["nf_total_carbohydrate"]
        }
    else:
        return None

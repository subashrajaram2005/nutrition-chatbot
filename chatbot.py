import re
from api.nutritionix_api import get_nutrition
import pandas as pd

custom_map = {
    "peanut butter": "peanut butter",
    "masala dosa": "masala dosa",
    "curd rice": "curd rice",
}


def normalize_query(query):
    for key in custom_map:
        if key in query.lower():
            return custom_map[key]
    return query


def get_from_csv(food_item):
    try:
        df = pd.read_csv("data/south_indian_foods.csv")
        match = df[df["Food"].str.lower().str.contains(food_item.lower())]
        if not match.empty:
            row = match.iloc[0]
            return {
                "name": row["Food"],
                "calories": row["Calories"],
                "protein": row["Protein (g)"],
                "fat": row["Fat (g)"],
                "carbs": row["Carbs (g)"]
            }
    except Exception as e:
        print(f"⚠️ CSV error: {e}")
    return None


def parse_quantity_and_food(query):
    pattern = r"(\d+)?\s*([a-zA-Z\s]+)"
    matches = re.findall(pattern, query.lower())

    results = []
    for qty_str, food_name in matches:
        qty = int(qty_str) if qty_str else 1
        food_name = food_name.strip()
        if food_name:
            results.append((qty, food_name))
    return results


def is_meal_request(query):
    # Check if user wants a meal suggestion by calories or protein
    calorie_match = re.search(r"(\d+)\s*calorie", query.lower())
    protein_match = re.search(r"(\d+)\s*gram protein", query.lower())
    if calorie_match:
        return ("calorie", int(calorie_match.group(1)))
    elif protein_match:
        return ("protein", int(protein_match.group(1)))
    else:
        return None


def suggest_meals(target_type, target_amount, df):
    col_map = {
        "calorie": "Calories",
        "protein": "Protein (g)"
    }
    results = []
    total = 0

    # Filter out very low calorie/protein items (threshold: 50 kcal or g)
    filtered_df = df[df[col_map[target_type]] > 50]

    # Sort descending to pick higher calorie/protein foods first
    sorted_df = filtered_df.sort_values(by=col_map[target_type], ascending=False)

    added_foods = set()
    for _, row in sorted_df.iterrows():
        food_name = row["Food"]
        val = row[col_map[target_type]]

        if total + val <= target_amount * 1.1 and food_name not in added_foods:
            results.append(food_name)
            added_foods.add(food_name)
            total += val

        if total >= target_amount * 0.9:
            break
    return results, total


print("🥗 Welcome to NutriBot! Ask me about any food item (type 'exit' to stop)")

df_foods = pd.read_csv("data/south_indian_foods.csv")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    meal_req = is_meal_request(user_input)
    if meal_req:
        target_type, target_amount = meal_req
        suggested_foods, total = suggest_meals(target_type, target_amount, df_foods)
        if suggested_foods:
            print(f"🍽️ Here's a suggested meal to meet your {target_amount} {target_type} target:")
            for food in suggested_foods:
                print(f"- {food}")
            print(f"Total {target_type}: {total:.1f}\n")
        else:
            print("Sorry, couldn't find a meal matching your target.\n")
        continue

    user_input = normalize_query(user_input)
    items_with_qty = parse_quantity_and_food(user_input)
    found = False

    # Accumulate totals
    total_calories = 0
    total_protein = 0
    total_fat = 0
    total_carbs = 0

    for qty, item in items_with_qty:
        result = get_nutrition(item)
        if not result:
            result = get_from_csv(item)

        if result:
            cal = float(result['calories']) * qty
            prot = float(result['protein']) * qty
            fat = float(result['fat']) * qty
            carb = float(result['carbs']) * qty

            total_calories += cal
            total_protein += prot
            total_fat += fat
            total_carbs += carb

            print(f"\n {result['name'].title()}:")
            print(
                f"   {qty} serving(s) contain about {cal:.1f} calories, {prot:.1f} g protein, {fat:.1f} g fat, and {carb:.1f} g carbs.")
            found = True
        else:
            print(f"\nSorry, I couldn't find nutrition info for '{item}'.")

    if found:
        print(f"\n📊 Nutrition Summary for all items:")
        print(f"Calories: {total_calories:.1f} kcal")
        print(f"Protein: {total_protein:.1f} g")
        print(f"Fat: {total_fat:.1f} g")
        print(f"Carbs: {total_carbs:.1f} g\n")
    else:
        print("Sorry, I couldn't fetch the nutrition info.\n")

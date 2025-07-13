# 🥗 NutriBot – A Smart Nutrition Chatbot

NutriBot is a Python-based command-line chatbot that helps users explore nutritional information of Indian foods. It supports natural language queries, quantity parsing (e.g., “2 idlis”), personalized meal suggestions based on calorie or protein goals, and uses both API and CSV data sources.

---

## 📌 Features

- 🍽️ **Chatbot Interface** – Ask in plain English like “Tell me about masala dosa”
- 📦 **Data Sources** – Uses Nutritionix API + custom CSV (South Indian foods)
- 🔍 **Food & Quantity Recognition** – Understands “2 idlis”, “1 cup of rasam” etc.
- 📊 **Nutrition Breakdown** – Returns calories, protein, fat, and carbs
- 🧠 **Smart Meal Suggestions** – Like “I want a 500 calorie meal”
- 🧾 **Nutrition Summary** – Shows total macros for all requested items
- ❌ **Duplicate & Spice Filtering** – Filters low-calorie repeated items

---

## ⚙️ Tech Stack

- **Python 3.x**
- `NLTK` – for natural language parsing
- `Pandas` – for CSV handling & suggestions
- `Requests` – for API integration
- Nutritionix API (optional)

---

## 🗂 Project Structure


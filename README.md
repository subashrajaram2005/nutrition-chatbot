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
nutrition-chatbot/
├── api/
│ └── nutritionix_api.py # Handles API requests
├── nlp/
│ └── extractor.py # Extracts food names and quantities from user input
├── data/
│ └── south_indian_foods.csv # Custom dataset with 500+ Indian food items
├── .env # Stores Nutritionix API credentials
├── .gitignore # Ignores .venv, .env, etc.
├── chatbot.py # Main chatbot script
├── requirements.txt # Python dependencies
└── README.md # Project documentation



---

# 🚀 How to Run Locally

# 1. Clone the Repository
git clone https://github.com/subashrajaram2005/nutrition-chatbot.git
cd nutrition-chatbot

# 2. Create a virtual environment
python -m venv .venv
.venv\Scripts\activate   # For Windows
# source .venv/bin/activate  # For macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the chatbot
python chatbot.py






import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def extract_food_items(query):
    tokens = word_tokenize(query.lower())
    keywords = [word for word in tokens if word.isalpha()]
    return keywords

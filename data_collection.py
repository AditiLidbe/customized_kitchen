import requests

def get_recipes(api_key, query, number=100):
    url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}&number={number}&apiKey={api_key}"
    response = requests.get(url)
    return response.json()

# Replace with your actual Spoonacular API key
api_key = "0cb7867b9ba1456991ceb895b4e0664c"
recipes = get_recipes(api_key, "pasta")

# Example: Print recipe titles
for recipe in recipes['results']:
    print(recipe['title'])

from flask import Flask, jsonify, request
import random

app = Flask(__name__)

recipes = [
    {"name": "Spaghetti Carbonara", "ingredients": ["spaghetti", "egg", "bacon", "cheese"]},
    {"name": "Vegan Tacos", "ingredients": ["tortilla", "avocado", "tomato", "lettuce", "beans"]},
    {"name": "Gluten-Free Pancakes", "ingredients": ["gluten-free flour", "milk", "egg", "butter"]},
]

@app.route('/recommend', methods=['POST'])
def recommend_recipe():
    data = request.get_json()
    ingredients = data.get('ingredients', [])
    dietary = data.get('dietary', "")

    # Simple matching based on ingredients
    matching_recipes = []
    for recipe in recipes:
        if all(item in ingredients for item in recipe['ingredients']):
            matching_recipes.append(recipe)

    if not matching_recipes:
        return jsonify({"message": "No matching recipes found."}), 404
    return jsonify({"recipes": matching_recipes})

if __name__ == '__main__':
    app.run(debug=True)
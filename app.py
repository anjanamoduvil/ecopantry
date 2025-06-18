from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

recipes_data = [
    {
        "name": "Leftover Veggie Salad",
        "filename": "salad.png",
        "desc": "Crunchy salad using leftovers from your fridge.",
        "page": "leftover-salad.html"
    },
    {
        "name": "Quick Fried Rice",
        "filename": "fried_rice.png",
        "desc": "A delicious way to reuse leftover rice with a burst of flavor.",
        "page": "quick-fried-rice.html"
    },
    {
        "name": "Banana Bread",
        "filename": "banana.png",
        "desc": "Overripe bananas? Make delicious banana bread instead!",
        "page": "banana-bread.html"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hub')
def hub():
    return render_template('hub.html')

@app.route('/recipes')
def recipes():
    return render_template("recipes.html", recipes=recipes_data)

@app.route('/search_recipe')
def search_recipe():
    query = request.args.get('query', '').strip().lower()
    for recipe in recipes_data:
        if query in recipe['name'].lower():
            return jsonify({"found": True, "recipe": recipe})
    return jsonify({"found": False})

@app.route('/share')
def share():
    return '<h2>Share Recipe Page</h2>'

@app.route('/zero_waste')
def zero_waste():
    return '<h2>Zero Waste Tips Page</h2>'

if __name__ == '__main__':
    app.run(debug=True)
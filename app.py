from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
shared_folder = os.path.join("templates", "shared")
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(shared_folder, exist_ok=True)

# Predefined recipes with existing HTML files in /templates/
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
# Load shared recipes
shared_data_path = 'data/shared_recipes.json'
if os.path.exists(shared_data_path):
    with open(shared_data_path, 'r') as file:
        shared_recipes = json.load(file)
else:
    shared_recipes = []

@app.route('/')
def fridge():
    return render_template('fridge.html')

@app.route('/hub')
def hub():
    return render_template('hub.html')

@app.route('/recipes')
def recipes():
    all_recipes = recipes_data + shared_recipes
    return render_template("recipes.html", recipes=all_recipes)

@app.route('/search_recipe')
def search_recipe():
    query = request.args.get('query', '').strip().lower()
    all_recipes = recipes_data + shared_recipes
    for recipe in all_recipes:
        if query in recipe['name'].lower():
            return jsonify({"found": True, "recipe": recipe})
    return jsonify({"found": False})

@app.route('/share', methods=['GET', 'POST'])
def share():
    if request.method == 'POST':
        name = request.form.get('name')
        title = request.form.get('title')
        ingredients = request.form.get('ingredients')
        instructions = request.form.get('instructions')
        file = request.files.get('video')

        filename = "default.png"
        if file and file.filename:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        page_filename = secure_filename(title.lower().replace(' ', '_')) + ".html"
        page_path = os.path.join("shared", page_filename)

        # Save recipe info
        new_recipe = {
            "name": title,
            "desc": f"Submitted by {name}",
            "filename": f"uploads/{filename}",
            "page": page_path
        }

        shared_recipes.append(new_recipe)
        with open(shared_data_path, 'w') as f:
            json.dump(shared_recipes, f, indent=2)

        # Create HTML file
        full_template_path = os.path.join("templates", page_path)
        with open(full_template_path, "w", encoding="utf-8") as f:
            f.write(f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
</head>
<body>
  <h1>{title}</h1>
  <p><strong>Submitted by:</strong> {name}</p>
  <h3>Ingredients:</h3>
  <p>{ingredients.replace('\n', '<br>')}</p>
  <h3>Instructions:</h3>
  <p>{instructions.replace('\n', '<br>')}</p>
  <img src="/static/{new_recipe['filename']}" alt="Recipe Image" width="300">
</body>
</html>""")

        return redirect(url_for('recipes'))

    return render_template('share.html')



# Serve user-created recipe pages from templates/shared
@app.route('/shared/<page_name>')
def shared_recipe_page(page_name):
    return render_template(f"shared/{page_name}")
# Route for predefined recipe: Leftover Salad
@app.route('/leftover-salad.html')
def leftover_salad():
    return render_template('leftover-salad.html')

# Route for predefined recipe: Quick Fried Rice
@app.route('/quick-fried-rice.html')
def quick_fried_rice():
    return render_template('quick-fried-rice.html')

# Route for predefined recipe: Banana Bread
@app.route('/banana-bread.html')
def banana_bread():
    return render_template('banana-bread.html')
@app.route('/zero_waste')
def zero_waste():
    return render_template('zero_waste.html')

if __name__ == '__main__':
    app.run(debug=True)
const form = document.getElementById('ingredientForm');
const results = document.getElementById('recipeResults');

const dummyRecipes = {
  rice: ["Veg Fried Rice", "Lemon Rice", "Rice Pancakes"],
  tomato: ["Tomato Soup", "Tomato Pasta"],
  onion: ["Onion Pakora", "Grilled Onions"],
  egg: ["Scrambled Egg", "Egg Fried Rice"],
};

form.addEventListener('submit', function (e) {
  e.preventDefault();
  const input = document.getElementById('ingredients').value.toLowerCase();
  const ingredients = input.split(',').map(i => i.trim());
  let suggestions = [];

  ingredients.forEach(ingredient => {
    if (dummyRecipes[ingredient]) {
      suggestions.push(...dummyRecipes[ingredient]);
    }
  });

  if (suggestions.length > 0) {
    results.innerHTML = `<h3>Recipes You Can Try:</h3><ul>${suggestions.map(r => `<li>${r}</li>`).join('')}</ul>`;
  } else {
    results.innerHTML = `<p>No recipes found for these ingredients. Try adding common items like rice, tomato, or onion.</p>`;
  }
});

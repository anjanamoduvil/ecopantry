document.getElementById("searchInput").addEventListener("input", function () {
  const query = this.value.toLowerCase().trim();
  const cards = document.querySelectorAll(".recipe-card");
  const noResults = document.getElementById("noResults");

  fetch('/search_recipe?query=${encodeURIComponent(query)}')
    .then(response => response.json())
    .then(data => {
      if (data.found) {
        cards.forEach(card => {
          const name = card.getAttribute("data-name").toLowerCase();
          card.style.display = name.includes(query) ? "block" : "none";
        });
        noResults.style.display = "none";
      } else {
        cards.forEach(card => card.style.display = "none");
        noResults.style.display = "block";
      }
    });
});
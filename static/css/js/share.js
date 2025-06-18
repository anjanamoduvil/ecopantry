const form = document.getElementById('recipeForm');
const confirmation = document.getElementById('confirmation');

form.addEventListener('submit', function (e) {
  e.preventDefault();

  const videoFile = document.getElementById('video').files[0];

  if (videoFile) {
    console.log("Video file selected:", videoFile.name);
    // You can process it with fetch() if integrating backend later
  }

  // Show confirmation message
  confirmation.style.display = 'block';

  // Reset form after submission
  form.reset();
});

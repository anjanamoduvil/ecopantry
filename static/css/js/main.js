// Simple fade in for page on load
document.addEventListener("DOMContentLoaded", () => {
  document.body.style.opacity = "0";
  document.body.style.transition = "opacity 1.5s ease-in-out";
  setTimeout(() => {
    document.body.style.opacity = "1";
  }, 100);
});

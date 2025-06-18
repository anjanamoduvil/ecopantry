// Animate on scroll
const fadeElems = document.querySelectorAll('.fade-in-up, .fade-slide-down, .fade-in');

const appearOnScroll = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    entry.target.classList.add('appear');
    observer.unobserve(entry.target);
  });
}, {
  threshold: 0.1,
  rootMargin: "0px 0px -50px 0px"
});

fadeElems.forEach(elem => {
  appearOnScroll.observe(elem);
});

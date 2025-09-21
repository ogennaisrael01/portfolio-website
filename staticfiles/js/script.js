// script.js
// Small utilities: close mobile nav on link click, typing effect, reveal on scroll

document.addEventListener('DOMContentLoaded', function () {
  // Close mobile nav when a link is clicked
  const navToggle = document.querySelector('#nav-toggle');
  const navLinks = document.querySelectorAll('nav a');
  navLinks.forEach(a => a.addEventListener('click', () => {
    if (navToggle && window.getComputedStyle(document.querySelector('.menu-icon')).display !== 'none') {
      navToggle.checked = false;
    }
  }));

  // Typing effect (home page)
  const typingEl = document.getElementById('typing-text');
  if (typingEl) {
    const phrases = [
      'Backend Developer • Django & Python',
      'Automation • API Design • Testing',
      'Building scalable, reliable systems'
    ];
    let pi = 0, ci = 0, typing = true;
    const typeSpeed = 40, pause = 1200, eraseSpeed = 20;
    function typeLoop() {
      const phrase = phrases[pi];
      if (typing) {
        typingEl.textContent = phrase.slice(0, ++ci);
        if (ci === phrase.length) {
          typing = false;
          setTimeout(typeLoop, pause);
        } else setTimeout(typeLoop, typeSpeed);
      } else {
        typingEl.textContent = phrase.slice(0, --ci);
        if (ci === 0) {
          typing = true;
          pi = (pi + 1) % phrases.length;
          setTimeout(typeLoop, 200);
        } else setTimeout(typeLoop, eraseSpeed);
      }
    }
    typeLoop();
  }

  // Reveal on scroll (simple IntersectionObserver)
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('revealed');
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
});

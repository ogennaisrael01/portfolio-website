document.addEventListener("DOMContentLoaded", () => {
  const texts = [
    "Backend Developer",
    "Python & Django Specialist",
    "Problem Solver",
    "I build scalable web applications"
  ];
  
  let count = 0;
  let index = 0;
  let currentText = "";
  let letter = "";
  const typingElement = document.getElementById("typing-text");

  function type() {
    if (count === texts.length) {
      count = 0;
    }
    currentText = texts[count];
    letter = currentText.slice(0, ++index);

    typingElement.textContent = letter;
    if (letter.length === currentText.length) {
      count++;
      index = 0;
      setTimeout(type, 1200); // pause before next word
    } else {
      setTimeout(type, 120);
    }
  }

  type();
});

const questions = document.querySelectorAll(".question");
const nextButton = document.querySelectorAll(".next");

let currentQuestion = 0;

function showQuestion() {
  questions[currentQuestion].classList.add("active");
}

function hideQuestion() {
  questions[currentQuestion].classList.remove("active");
}

function nextQuestion() {
  hideQuestion();
  currentQuestion++;
  if (currentQuestion < questions.length) {
    showQuestion();
  } else {
    document.querySelector("form").submit();
  }
}


showQuestion();

nextButton.forEach(button => {
  button.addEventListener("click", nextQuestion);
});



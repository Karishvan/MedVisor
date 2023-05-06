const questions = document.querySelectorAll(".question");
const nextButton = document.querySelectorAll(".next");
let results = "";

let currentQuestion = 0;

function showQuestion() {
  questions[currentQuestion].classList.add("active");
}

function hideQuestion() {
  questions[currentQuestion].classList.remove("active");
}

function nextQuestion() {
  const response = getResponse();
  results += ". " + response;
  console.log("CURRENT RESULTS ARE " + results)
  hideQuestion();
  currentQuestion++;
  if (currentQuestion < questions.length) {
    showQuestion();
  } else {
    document.querySelector("form").submit();
  }
}

function getResponse() {
  const question = questions[currentQuestion];
  const responseElement = question.querySelector(".response");
  if (responseElement.querySelector("input[type=radio]")) {
    const checkedInput = responseElement.querySelector("input[type=radio]:checked");
    return checkedInput.value;
  } else if (responseElement.querySelector("input[type=range]")) {
    const rangeInput = responseElement.querySelector("input[type=range]");
    return rangeInput.value;
  } else if (responseElement.querySelector("input[type=text]")) {
    const textInput = responseElement.querySelector("input[type=text]");
    return textInput.value;
  }
}

showQuestion();

nextButton.forEach(button => {
  button.addEventListener("click", nextQuestion);
});

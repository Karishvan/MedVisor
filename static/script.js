const questions = document.querySelectorAll(".question");
const nextButton = document.querySelectorAll(".next");
let userSymptomsSummary = "";

console.log(questions);
let currentQuestion = 0;

function showQuestion() {
  console.log(questions[currentQuestion])
  questions[currentQuestion].classList.add("active");
}

function hideQuestion() {
  questions[currentQuestion].classList.remove("active");
}

function nextQuestion() {
  const response = getResponse();
  userSymptomsSummary += ". " + response;
  console.log("CURRENT SUMMARY IS: " + userSymptomsSummary)
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
    const rangeValue = rangeInput.value;
    let painTitle;
    if (rangeValue >= 0 && rangeValue <=2){
      painTitle = "mild"; 
    } else if (rangeValue >= 3 && rangeValue <= 5){
      painTitle = "medium"
    } else {
      painTitle = "severe"
    }
    return painTitle;
  } else if (responseElement.querySelector("input[type=text]")) {
    const textInput = responseElement.querySelector("input[type=text]");
    return textInput.value;
  }
}

showQuestion();

nextButton.forEach(button => {
  button.addEventListener("click", nextQuestion);
});


const form = document.querySelector('form');
const resultDiv = document.querySelector('#result');
form.addEventListener('submit', (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  fetch('/calculate', {
      method: 'POST',
      body: formData
  })
  .then(response => response.json())
  .then(data => {
      resultDiv.innerHTML = `Result: ${data.result}`;
  });
});


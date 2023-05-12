const questions = document.querySelectorAll(".question");
const nextButton = document.querySelectorAll(".next");
let userSymptomsSummary = "";

let currentQuestion = 0;

function showQuestion() {
  console.log(questions[currentQuestion].classList)
  questions[currentQuestion].classList.add("active");
}

function hideQuestion() {
  questions[currentQuestion].classList.remove("active");
}

function nextQuestion() {
  const response = getResponse();
  userSymptomsSummary += response;
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
    return "The severity of my pain out of ten is " + rangeInput.value + "/10. ";
  } else if (responseElement.querySelector("input[type=text]")) {
    const textInput = responseElement.querySelector("input[type=text]");
    return textInput.value + ". ";
  }
}

showQuestion();

nextButton.forEach(button => {
  button.addEventListener("click", nextQuestion);
});



const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(form);

    fetch('/calculate', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            const result = encodeURIComponent(formData.get('userSymptomsSummary'));
            const url = `/results?result=${result}`;
            window.location.href = url;  // Redirect to the results page with the query parameter
        } else {
            throw new Error('Error occurred during calculation');
        }
    })
    .catch(error => {
        console.log('An error occurred:', error);
    });
});




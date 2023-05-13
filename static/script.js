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


/* 
const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(form);
    console.log("CURRENT USER SYMPTOMS SUMM IS " + userSymptomsSummary)
    formData.append('userSymptomsSummary', userSymptomsSummary); // Add the userSymptomsSummary value to the form data
    
    fetch('/calculate', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            const result = encodeURIComponent(response);
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
 */


const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(form);
    console.log("CURRENT USER SYMPTOMS SUMM IS " + userSymptomsSummary)
    formData.append('userSymptomsSummary', userSymptomsSummary); // Add the userSymptomsSummary value to the form data
    fetch('/endpoint', {
      method: 'POST',
      body: formData
    })
    fetch('/calculate', {
      method: 'POST',
      body: formData
    })
    .then(response => {
      if (response.ok) {
          return response.json(); // Parse the response as JSON
      } else {
          throw new Error('Error occurred during calculation');
      }
    })
    .then(result => {
      const calcResp = result.result; // Extract the 'result' property from the response
      const encodedResult = encodeURIComponent(calcResp);
      const url = `/results?result=${encodedResult}`;
      window.location.href = url; // Redirect to the results page with the query parameter
    })
    .catch(error => {
        console.log('An error occurred:', error);
    });
});


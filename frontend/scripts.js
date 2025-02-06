document.addEventListener("DOMContentLoaded", function () {
    // Get current page URL
    const currentPage = window.location.pathname.split("/").pop();

    // Get all nav links
    const navLinks = document.querySelectorAll(".header-nav-links a");

    // Loop through links and check if href matches the current page
    navLinks.forEach(link => {
        if (link.getAttribute("href") === currentPage) {
            link.classList.add("active");
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const troubleshootOptions = document.querySelectorAll(".troubleshoot-options .card");
    const symptomsContainer = document.getElementById("symptoms-list");
    const followUpQuestionsContainer = document.getElementById("follow-up-questions");

    // Function to fetch symptoms based on selected sense
    function fetchSymptoms(sense) {
        fetch(`http://localhost:5000/api/symptoms/sensation/${sense}`)
            .then(response => response.json())
            .then(data => {
                // console.log(data);
                displaySymptoms(data);
            })
            .catch(error => console.error("Error fetching symptoms:", error));
    }

    // Function to display symptoms
    function displaySymptoms(symptoms) {
        symptomsContainer.innerHTML = ""; // Clear previous symptoms
        symptoms.forEach(symptom => {
            const symptomItem = document.createElement("div");
            symptomItem.classList.add("symptom-item");
            symptomItem.textContent = symptom.symptom_text;
            symptomItem.setAttribute("data-symptom-id", symptom.id); // Store symptom id for further use

            // Add event listener to handle symptom selection
            symptomItem.addEventListener("click", function () {
                const symptomId = this.getAttribute("data-symptom-id");
                fetchFollowUpQuestions(symptomId);
            });

            symptomsContainer.appendChild(symptomItem);
        });
    }

    // Function to fetch follow-up questions based on selected symptom
    function fetchFollowUpQuestions(symptomId) {
        fetch(`http://localhost:5000/api/questions/symptom/${symptomId}`)
            .then(response => response.json())
            .then(data => {
                displayFollowUpQuestions(data);
            })
            .catch(error => console.error("Error fetching follow-up questions:", error));
    }

    // Function to display follow-up questions
    function displayFollowUpQuestions(questions) {
        followUpQuestionsContainer.innerHTML = ""; // Clear previous follow-up questions
        questions.forEach(question => {
            const questionItem = document.createElement("div");
            questionItem.classList.add("question-item");
            questionItem.textContent = question.question_text;
            questionItem.setAttribute("data-question-id", question.id); // Store question id for further use

            // Add event listener for selecting the answer
            questionItem.addEventListener("click", function () {
                const questionId = this.getAttribute("data-question-id");
                // Process answer selection (you could use a modal or input field for this)
                displayResult(questionId); // Call function to display the result based on answer
            });

            followUpQuestionsContainer.appendChild(questionItem);
        });
    }

    // Function to display the final result after follow-up question selection
    function displayResult(questionId) {
        // Fetch the result based on the question and answer (this could be a yes/no or other response type)
        fetch(`http://localhost:5000/api/problems/question/${questionId}`)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Display result (problem description and solution)
                const resultText = `Problem: ${data[0].problem_description}`;
                alert(resultText); // Display result in an alert or modal
            })
            .catch(error => console.error("Error fetching result:", error));
    }

    // Add event listeners to the sensation cards
    troubleshootOptions.forEach(card => {
        card.addEventListener("click", function () {
            const sense = this.getAttribute("data-type"); // Get the sense type (see, hear, feel, smell)
            fetchSymptoms(sense);
        });
    });
});


function toggleMenu() {
    document.querySelector(".header-nav-links").classList.toggle("active");
}
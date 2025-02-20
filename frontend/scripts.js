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
    let selectedSymptom = null; // Track selected symptom

    function fetchSymptoms(sense) {
        fetch(`http://localhost:5000/api/symptoms/sensation/${sense}`)
            .then(response => response.json())
            .then(data => {
                displaySymptoms(data);
            })
            .catch(error => console.error("Error fetching symptoms:", error));
    }

    function displaySymptoms(symptoms) {
        symptomsContainer.style.display = "block";
        followUpQuestionsContainer.style.display ="none";
        symptomsContainer.innerHTML = ""; // Clear previous symptoms
        followUpQuestionsContainer.innerHTML = ""; // Clear follow-up questions
        selectedSymptom = null; // Reset selected symptom

        const title = document.createElement("h3");
        title.textContent = "Which symptom do you see on your car?";
        title.classList.add("symptom-title"); // Optional: Add a class for styling
        symptomsContainer.appendChild(title);

        symptoms.forEach(symptom => {
            const symptomItem = document.createElement("div");
            symptomItem.classList.add("symptom-item");
            symptomItem.textContent = symptom.symptom_text;
            symptomItem.setAttribute("data-symptom-id", symptom.id);

            symptomItem.addEventListener("click", function () {
                // Remove highlight from previous selection
                if (selectedSymptom) {
                    selectedSymptom.classList.remove("selected-symptom");
                }

                // Highlight the selected symptom
                this.classList.add("selected-symptom");
                selectedSymptom = this;

                const symptomId = this.getAttribute("data-symptom-id");

                if (symptom.followup_available) {
                    fetchFollowUpQuestions(symptomId);
                } else {
                    // followUpQuestionsContainer.style.display = "none";
                    displayProblem(symptomId);
                }
                
            });

            symptomsContainer.appendChild(symptomItem);
        });
    }

    function fetchFollowUpQuestions(symptomId) {
        fetch(`http://localhost:5000/api/questions/symptom/${symptomId}`)
            .then(response => response.json())
            .then(data => {
                displayFollowUpQuestions(data);
            })
            .catch(error => console.error("Error fetching follow-up questions:", error));
    }

    function displayFollowUpQuestions(questions) {
        followUpQuestionsContainer.style.display = "block";
        followUpQuestionsContainer.innerHTML = ""; // Clear previous follow-up questions

        const title = document.createElement("h3");
        title.textContent = "Which describes your problem best?";
        title.classList.add("followup-title"); // Optional: Add a class for styling
        followUpQuestionsContainer.appendChild(title);

        questions.forEach(question => {
            const questionItem = document.createElement("div");
            questionItem.classList.add("question-item");
            questionItem.textContent = question.question_text;
            questionItem.setAttribute("data-question-id", question.id);

            questionItem.addEventListener("click", function () {
                const questionId = this.getAttribute("data-question-id");
                displayResult(questionId);
            });

            followUpQuestionsContainer.appendChild(questionItem);
        });
    }

    function displayResult(questionId) {
        fetch(`http://localhost:5000/api/problems/question/${questionId}`)
            .then(response => response.json())
            .then(data => {
                alert(`Problem: ${data[0].problem_description}\nSolution: ${data[0].solution}`);
            })
            .catch(error => console.error("Error fetching result:", error));
    }

    function displayProblem(symptomId) {
        fetch(`http://localhost:5000/api/problems/symptom/${symptomId}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Server error: ${response.status}`);
                }
                return response.text(); // Read as text first
            })
            .then(text => {
    
                try {
                    const data = JSON.parse(text); // Try to parse JSON
                    if (data.length > 0) {
                        alert(`Problem: ${data[0].problem_description}\nSolution: ${data[0].solution}`);
                    } else {
                        alert("No problem found for this symptom.");
                    }
                } catch (error) {
                    console.error("Error parsing JSON:", error, "Response was:", text);
                }
            })
            .catch(error => console.error("Error fetching result:", error));
    }
    

    troubleshootOptions.forEach(card => {
        card.addEventListener("click", function () {
            const sense = this.getAttribute("data-type");
            fetchSymptoms(sense);
        });
    });
});



function toggleMenu() {
    document.querySelector(".header-nav-links").classList.toggle("active");
}

function openModal() {
    document.getElementById("obdModal").style.display = "block";
}

function closeModal() {
    document.getElementById("obdModal").style.display = "none";
    document.getElementById("obdResult").innerHTML = "";
    document.getElementById("obdInput").value = "";
}

async function lookupOBD() {
    const obdCode = document.getElementById("obdInput").value.trim().toUpperCase();
    const obdResult = document.getElementById("obdResult");

    if (!obdCode) {
        obdResult.innerHTML = `<div class="alert alert-danger">Please enter an OBD code.</div>`;
        return;
    }

    try {
        const response = await fetch(`http://localhost:5000/api/obd/code/${obdCode}`);
        
        if (!response.ok) {
            throw new Error("OBD Code not found.");
        }

        const data = await response.json();

        if (data.description) {
            obdResult.innerHTML = `<div class="alert alert-success">
                <strong>${obdCode}:</strong> ${data.description}
            </div>`;
        } else {
            obdResult.innerHTML = `<div class="alert alert-danger">OBD Code not found.</div>`;
        }
    } catch (error) {
        obdResult.innerHTML = `<div class="alert alert-danger">Error: ${error.message}</div>`;
    }
}

// Click event listeners for navbar link and hero card
document.getElementById("obdNavLink").addEventListener("click", openModal);
document.getElementById("obdHeroCard").addEventListener("click", openModal);

// Close modal if clicking outside content
window.onclick = function(event) {
    const modal = document.getElementById("obdModal");
    if (event.target === modal) {
        closeModal();
    }
}

async function fetchTip() {
    try {
        const response = await fetch('http://localhost:5000/api/tips/');
        const tips = await response.json();
        if (tips.length > 0) {
            const randomTip = tips[Math.floor(Math.random() * tips.length)];
            document.getElementById('tipShort').textContent = randomTip.tip_short;
            document.getElementById('tipLong').textContent = randomTip.tip_long;
        }
        document.getElementById('tipBox').style.display = 'block';
        document.getElementById('overlay').style.display = 'block';
    } catch (error) {
        console.error('Error fetching tips:', error);
        document.getElementById('tipShort').textContent = 'Failed to load tip.';
        document.getElementById('tipLong').textContent = '';
    }
}

function closeTip() {
    document.getElementById('tipBox').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
}

document.getElementById("car_tips_1").addEventListener("click", fetchTip);
document.getElementById("car_tips_2").addEventListener("click", fetchTip);
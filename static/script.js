document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("prediction-form").addEventListener("submit", function(e) {
        e.preventDefault();

        let formData = {
            gender: document.getElementById("gender").value,
            age: parseInt(document.getElementById("age").value),
            hypertension: parseInt(document.getElementById("hypertension").value),
            heart_disease: parseInt(document.getElementById("heart_disease").value),
            ever_married: document.getElementById("ever_married").value,
            work_type: document.getElementById("work_type").value,
            residence_type: document.getElementById("residence_type").value,
            avg_glucose_level: parseFloat(document.getElementById("avg_glucose_level").value),
            bmi: parseFloat(document.getElementById("bmi").value),
            smoking_status: document.getElementById("smoking_status").value
        };

        fetch("http://127.0.0.1:5000/api/data", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("result-container").style.display = "block";
            document.getElementById("prediction-result").innerText = "Stroke Prediction: " + data.result;
        })
        .catch(error => console.error("Error:", error));
    });
});

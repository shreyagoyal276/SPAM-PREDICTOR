// document.addEventListener("DOMContentLoaded", function () {
//     const form = document.querySelector("form");
//     const messageBox = document.getElementById("message");

//     form.addEventListener("submit", function (event) {
//         if (!messageBox.value.trim()) {
//             alert("Please enter a message!");
//             event.preventDefault(); // Prevents form submission if input is empty
//         }
//     });
// });
fetch("http://127.0.0.1:5000/predict", {  // Now using local Flask API
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: userMessage })
})
.then(response => response.json())
.then(data => {
    document.getElementById("result").innerText = data.prediction === "Spam" ? "🚨 Spam Detected!" : "✅ Not Spam!";
})
.catch(error => console.error("Error:", error));

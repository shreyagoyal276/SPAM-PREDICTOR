from flask import Flask, render_template, request
app = Flask(__name__)


def check_spam(message):
    spam_words = ["win", "free", "lottery", "money", "otp", "click here"]
    is_spam = any(word in message.lower() for word in spam_words)
    return "🚨 Spam Detected!" if is_spam else "✅ Not Spam!"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""  
    message = ""
    
    if request.method == "POST":
        message = request.form.get("message", "").strip()
        if message:
            result = check_spam(message)
    
    return render_template("index.html", result=result, message=message)

if __name__ == "__main__":
    app.run(debug=True)









# from flask import Flask, request, jsonify
# #import requests

# app = Flask(__name__)

# # Replace with your Google Colab API URL
# COLAB_API_URL = "http://<your-colab-ip>:8000/predict"

# @app.route("/predict", methods=["POST"])
# def predict():
#     data = request.get_json()
#     if "message" not in data:
#         return jsonify({"error": "Message text required"}), 400

#     # Send request to Colab API
#     response = requests.post(COLAB_API_URL, json=data)
#     return jsonify(response.json())

# if __name__ == "__main__":
#     app.run(debug=True)





# function checkSpam(){
#     const message = document.getElementById("message").value.trim();
    
#     if (!message) {
#         alert("Please enter a message!");
#         return;
#     }

#     fetch("https://<your-colab-ip>:8000/predict", {  // Replace with your Colab API URL
#     method: "POST",
#     headers: {
#         "Content-Type": "application/json"
#     },
#     body: JSON.stringify({ message: message })
# })
# .then(response => response.json())
# .then(data => {
#     document.getElementById("result").innerText = data.prediction === "Spam" ? "🚨 Spam Detected!" : "✅ Not Spam!";
# })
# .catch(error => console.error("Error:", error));

#     .then(response => response.json())
#     .then(data => {
#         document.getElementById("result").innerText = data.prediction === "Spam" ? "🚨 Spam Detected!" : "✅ Not Spam!";
#     })
#     .catch(error => console.error("Error:", error));
# }

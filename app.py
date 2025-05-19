from flask import Flask, render_template, request
app = Flask(__name__)

import pickle
tfidf= pickle.load(open("vectorizer.pkl",'rb'))
model= pickle.load(open("model.pkl",'rb'))


def check_spam(message):
    transformed_message=tfidf.transform([message])
    if model.predict(transformed_message)[0]==1:
        return "🚨 Spam Detected!"
    else:
        return "✅ Not Spam!"

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








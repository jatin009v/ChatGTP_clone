from flask import Flask, render_template, jsonify, request
import openai

openai.api_key = "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"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def qa():
    if request.method == "POST":
        question = request.json.get("question")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        answer = response["choices"][0]["text"]
        data = {"question": question, "answer": answer}
        return jsonify(data)

    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss?"}
    return jsonify(data)

# UptimeRobot will ping this endpoint to keep the app alive
@app.route("/alive")
def alive():
    return "I'm alive!"

if __name__ == "__main__":
    app.run(debug=True, port=3000)

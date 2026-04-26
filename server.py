from flask import Flask, request, jsonify

app = Flask(__name__)

scores = []

@app.route("/")
def home():
    return "OK WORKING"

@app.route("/send", methods=["POST"])
def send():
    data = request.json

    name = data.get("name", "Player")
    score = data.get("score", 0)

    scores.append({
        "name": name,
        "score": score
    })

    # сортуємо по score
    scores.sort(key=lambda x: x["score"], reverse=True)

    # тільки топ 10
    scores[:] = scores[:10]

    return {"ok": True}

@app.route("/leaderboard")
def leaderboard():
    return jsonify(scores)

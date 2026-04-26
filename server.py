from flask import Flask, request, jsonify

app = Flask(__name__)

scores = []

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    score = data.get("score", 0)

    scores.append(score)
    scores.sort(reverse=True)
    scores[:] = scores[:10]

    return {"ok": True}

@app.route("/leaderboard")
def leaderboard():
    return jsonify(scores)

if __name__ == "__main__":
    app.run()
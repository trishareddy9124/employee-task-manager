from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Learn Git",
        "status": "Pending"
    },
    {
        "id": 2,
        "title": "Practice GitHub",
        "status": "Completed"
    }
]


@app.route("/")
def home():
    return jsonify({
        "message": "Employee Task Manager API is running successfully"
    })


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


if __name__ == "__main__":
    app.run(debug=True)
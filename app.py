from flask import Flask, jsonify, request

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


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "status": data.get("status", "Pending")
    }

    tasks.append(new_task)

    return jsonify(new_task), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data.get("title", task["title"])
            task["status"] = data.get("status", task["status"])

            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

            return jsonify({
                "message": "Task deleted successfully"
            })

    return jsonify({"error": "Task not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
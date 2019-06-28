from flask import make_response, jsonify, Flask, request, Blueprint, make_response
from app.models.tasks_model import Tasks

tasks = Blueprint('tasks', __name__, url_prefix='/taskMS/api/v1')

@tasks.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

    title = data['title']
    description = data['description']
    createdDate = data['createdDate']
    startDate = data['startDate']
    endDate = data['endDate']

    payload = Tasks(title, description)
    new_task = payload.create_task()
    response_message = {
        "status": "success",
        "message": "task created successfully"

    }
    return jsonify(new_task, response_message), 201

@tasks.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

@tasks.route('/tasks/<int:id>', methods=['GET'])
def get_task():
    return jsonify(tasks[int(id)-1])
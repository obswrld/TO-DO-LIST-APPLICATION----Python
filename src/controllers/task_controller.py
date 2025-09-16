from flask import Blueprint, request, jsonify
from src.services.task_service import TaskService

task_controller = Blueprint('task_controller', __name__)
task_service = TaskService()

@task_controller.route('/create', methods=['POST'])
def create_task():
    data = request.get_json()
    task = task_service.create_task(data['title'], data['description'], data['user_id'])
    required_fields = ['title', 'description', 'user_id']
    for field in required_fields:
        if field not in data:
            return jsonify({'message': 'Required field is missing'}), 400

    task = task_service.create_task(data['title'], data['description'], data['user_id'])
    return jsonify(task.to_dict()), 201

@task_controller.route('/retrieve', methods=['GET'])
def get_tasks():
    task = task_service.get_all_task()
    return jsonify([task.to_dict() for task in task]), 200

@task_controller.route('/retrieve/<int:task_id>', methods=['GET'])
def get_tasks_by_id(task_id):
    task = task_service.get_task_by_id(task_id)
    if task:
        return jsonify(task.to_dict()), 200
    return jsonify({'message': 'Task not Found'}), 404

@task_controller.route('/update/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    updated_task = task_service.update_task(task_id, data)
    if updated_task:
        return jsonify(updated_task.to_dict()), 200
    return jsonify({'message': 'Task not Found'}), 404

@task_controller.route('/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = task_service.delete_task(task_id)
    if task:
        return jsonify({'message': 'Task Not Found'}), 200
    return jsonify({'message': 'Task not Found'}), 404

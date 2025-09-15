from flask import Blueprint, request, jsonify

from src.services.task_service import TaskService

task_controller = Blueprint('task_controller', __name__)
task_service = TaskService()

@task_controller.route('/create_task', methods=['POST'])
def create_task():
    data = request.get_json()
    task = task_service.create_task(data)
    return jsonify(task.to_dict()), 201

@task_controller.route('/get_tasks', methods=['GET'])
def get_tasks(task_id):
    task = task_service.get_task_by_id(task_id)
    if task:
        return jsonify(task.to_dict()), 200
    return jsonify({'message': 'Task not Found'}), 404

@task_controller.route('/update_task', methods=['PUT'])
def update_task():
    data = request.get_json()
    updated_task = task_service.update_task(data)
    if updated_task:
        return jsonify(updated_task.to_dict()), 200
    return jsonify({'message': 'Task not Found'}), 404

@task_controller.route('/delete_task', methods=['DELETE'])
def delete_task(task_id):
    data = request.get_json()
    task = task_service.delete_task(task_id)
    if task:
        return jsonify(task.to_dict()), 200
    return jsonify({'message': 'Task not Found'}), 404

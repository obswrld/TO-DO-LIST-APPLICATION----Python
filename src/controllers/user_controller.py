from flask import Blueprint, request, jsonify
from src.services.user_Service import UserService

user_controller = Blueprint('user_controller', __name__)
user_service = UserService()

@user_controller.route('/register', methods=['POST'])
def register_user():
    data = request.json()
    user = user_service.create_user(data['username'], data['email'])
    return jsonify(user.to_dict()), 201

@user_controller.route('/login', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    return jsonify(users.to_dict()), 200

@user_controller.route('/login', methods=['GET'])
def get_user_by_id(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'message': 'User Not Found'}), 404

@user_controller.route('/logout', methods=['PUT'])
def update_user(user_id):
    data = request.json()
    updated_user = user_service.update_user(user_id, data)
    if updated_user:
        return jsonify(updated_user.to_dict()), 200
    return jsonify({'message': 'User Not Found'}), 404

@user_controller.route('/logout', methods=['DELETE'])
def delete_user(user_id):
    result = user_service.delete_user(user_id)
    if result:
        return jsonify(result), 200
    return jsonify({'message': 'User Not Found'}), 404

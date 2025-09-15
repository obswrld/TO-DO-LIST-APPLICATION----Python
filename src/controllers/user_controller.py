from flask import Blueprint, request, jsonify
from src.services.user_Service import UserService

user_controller = Blueprint('user_controller', __name__)
user_service = UserService()

@user_controller.route('/users', methods=['POST'])
def register_user():
    data = request.get_json()
    user = user_service.create_user(data['username'], data['email'], data['password'])
    return jsonify(user.to_dict()), 201

@user_controller.route('/users', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    return jsonify([user.to_dict() for user in users]), 200

@user_controller.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'message': 'User Not Found'}), 404

@user_controller.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    updated_user = user_service.update_user(user_id, data)
    if updated_user:
        return jsonify(updated_user.to_dict()), 200
    return jsonify({'message': 'User Not Found'}), 404

@user_controller.route('/logout', methods=['DELETE'])
def delete_user(user_id):
    result = user_service.delete_user(user_id)
    if result:
        return jsonify({'message': 'User Not Found'}), 200
    return jsonify({'message': 'User Not Found'}), 404

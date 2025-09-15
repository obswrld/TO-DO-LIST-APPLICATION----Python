from flask import Blueprint, request, jsonify
from src.services.label_service import LabelService

label_controller = Blueprint('label_controller', __name__)
label_service = LabelService()

@label_controller.route('/labels', methods=['POST'])
def create_label():
    data = request.get_json()
    label = LabelService.create_label(data['name'])
    return jsonify(label.to_dict()), 201

@label_controller.route('/labels', methods=['GET'])
def get_all_labels():
    labels = label_service.get_all_labels()
    return jsonify([label.to_dict() for label in labels]), 200

@label_controller.route('/label', methods=['PUT'])
def update_label(label_id):
    data = request.get_json()
    updated_label = LabelService.update_label(label_id, data)
    if updated_label:
        return jsonify(updated_label.to_dict()), 200
    return jsonify({'message': 'User Not Found'}), 400

@label_controller.route('/labels/<int:label_id>', methods=['DELETE'])
def delete_label(label_id):
    data = request.json()
    deleted_label = label_service.delete_label(label_id)
    if deleted_label:
        return jsonify({'message': 'User Not Found'}), 200
    return jsonify({'message': 'User Not Found'}), 400


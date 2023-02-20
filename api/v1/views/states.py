#!/usr/bin/python3
""" handles RESTful API actions for State objects """

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage, state


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """ retrieves the list of all State objects """
    states = storage.all(state.State).values()
    return jsonify([state.to_dict() for state in states])


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """ retrieves a State object """
    state = storage.get(state.State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """ deletes state object """
    state = storage.get(state.State, state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('states', methods=['POST'], strict_slashes=False)
def post_state():
    """ create a state """
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'name' not in request.get_json():
        abort(400, "Missing name")
    state = state.State(**request.get_json())
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """updates a state object"""
    if not request.get_json():
        abort(400, "Not a JSON")
    state = storage.get(state.State, state_id)
    if state is None:
        abort(404)
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200

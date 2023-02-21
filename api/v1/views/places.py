#!/usr/bin/python3
""" create view for place objects """


from api.v1.app import app_views
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.city import City


@app_views.route('/api/v1/cities/<city_id>/places', methods=['GET'])
def get_places(city_id):
    """ retrieves list of all places """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    place = city.places
    return jsonify([place.to_dict() for place in places])

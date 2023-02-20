#!/usr/bin/python3
"""route status on the
object app_views that returns a JSON: “status”: “OK”
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('status', strict_slashes=False)
def status():
    """ return status """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """retrieves the number of each objects by type"""
    from models import storage
    classes = {"amenities": "Amenity", "cities": "City",
               "places": "Place", "reviews": "Review",
               "states": "State", "users": "User"}
    count = {}
    for key, value in classes.items():
        count[key] = storage.count(value)
    return jsonify(count)

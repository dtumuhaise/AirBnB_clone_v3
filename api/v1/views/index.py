#!/usr/bin/python3
"""route status on the
object app_views that returns a JSON: “status”: “OK”
"""

from api.v1.views import app_views


@app.route('status', strict_slashes=False)
def status():
    """ return status """
    return jsonify({"status": "OK"})

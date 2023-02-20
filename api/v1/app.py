#!/usr/bin/python3
""" Flask app """

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
import os


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """ calls storage.close() """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """ 404 error handler """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)

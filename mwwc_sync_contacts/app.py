from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from mwwc_sync_contacts.external_services.airtable import get_banana_data

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return (
        f"{__name__}<p>The UI goes here.</p><p>{os.getenv('TEST_VAR', 'default')}</p>"
    )


@app.route("/sync-contacts")
def sync_contacts():
    try:
        banana_data = get_banana_data()
        return jsonify(banana_data)
    except Exception as e:
        message = {"error": f"An http error occurred: {e}"}
        return jsonify(message)


@app.route("/restore-backup")
def restore_backup():
    data = {"some": "backup"}
    return jsonify(data)

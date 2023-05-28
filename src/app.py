import sys
from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from src.external_services.airtable import get_banana_data

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return f"<p>The UI goes here.</p><p>{os.getenv('TEST_VAR', 'test var does not exist')}</p>"


@app.route("/sync-contacts")
def sync_contacts():
    banana_data = get_banana_data()
    return jsonify(banana_data)


@app.route("/restore-backup")
def restore_backup():
    data = {"some": "backup"}
    return jsonify(data)

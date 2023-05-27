from flask import Flask, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return f"<p>The UI goes here.</p><p>{os.getenv('TEST_VAR', 'test var does not exist')}</p>"

@app.route("/sync-contacts")
def sync_contacts():
    data = {"some": "contacts"}
    return jsonify(data)

@app.route("/restore-backup")
def restore_backup():
    data = {"some": "backup"}
    return jsonify(data)

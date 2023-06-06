from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from pathlib import Path
from mwwc_sync_contacts.external_services.airtable import get_banana_data
from mwwc_sync_contacts.external_services.google import get_google_workspace_client
from mwwc_sync_contacts.data_transformation.google import sync_google_workspace

load_dotenv()


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        AIRTABLE_API_KEY=os.environ["AIRTABLE_API_KEY"],
        AIRTABLE_BASE_ID=os.environ["AIRTABLE_BASE_ID"],
        AIRTABLE_TABLE_ID=os.environ["AIRTABLE_TABLE_ID"],
    )

    @app.route("/")
    def index():
        return f"""
        {__name__}
        <p>The UI goes here.</p><p>{os.getenv('TEST_VAR', 'default')}</p>
        """

    @app.route("/sync-contacts")
    def sync_contacts():
        try:
            # banana_data = get_banana_data(app.config)
            banana_data = []
            google_client = get_google_workspace_client()
            return jsonify([sync_google_workspace(google_client), banana_data])

        except Exception as e:
            message = {"error": f"An http error occurred: {e}"}
            return jsonify(message)

    @app.route("/restore-backup")
    def restore_backup():
        data = {"some": "backup"}
        return jsonify(data)

    return app

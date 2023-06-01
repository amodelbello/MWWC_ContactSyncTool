from __future__ import print_function
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from from_root import from_root

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/admin.directory.user"]


def get_google_workspace_client():
    creds = None
    path = from_root() / "gcp_creds"
    token_file = path / "token.json"
    credentials_file = path / "credentials.json"

    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_file,
                SCOPES,
            )
            creds = flow.run_local_server(port=8000)

        # Save the credentials for the next run
        with open(token_file, "w") as token:
            token.write(creds.to_json())

    client = build("admin", "directory_v1", credentials=creds)
    return client

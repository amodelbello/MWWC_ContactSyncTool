from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from mwwc_sync_contacts import get_project_root

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/admin.directory.user"]


def main():
    """Shows basic usage of the Admin SDK Directory API.
    Prints the emails and names of the first 10 users in the domain.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    path = get_project_root() / "gcp_creds"
    token_file = path / "token.json"
    credentials_file = path / "credentials.json"

    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
            creds = flow.run_local_server(port=8000)
        # Save the credentials for the next run
        with open(token_file, "w") as token:
            token.write(creds.to_json())

    service = build("admin", "directory_v1", credentials=creds)

    # Call the Admin SDK Directory API
    print("Getting the first 10 users in the domain")
    results = (
        service.users()
        .list(customer="my_customer", maxResults=10, orderBy="email")
        .execute()
    )
    users = results.get("users", [])

    if not users:
        print("No users in the domain.")
    else:
        print("Users:")
        for user in users:
            print("{0} ({1})".format(user["primaryEmail"], user["name"]["fullName"]))


if __name__ == "__main__":
    main()

import pytest
from unittest.mock import patch
from mwwc_google import GoogleWorkspace


"""
Need to mock:
- Investigate Magic mocks. Is this a way to not have to mock everything?
- from google.oauth2.credentials import Credentials
    - creds = Credentials.from_authorized_user_file(token_file, SCOPES)

"""


class TestGoogle:
    @patch('googleapiclient.discovery.build')
    def test_get_groups(
        self,
        mock_build,
        google_client,
    ):
        mock_build.client = google_client
        google_workspace = GoogleWorkspace(google_client)
        groups = google_workspace.groups

        assert (len(groups) > 0)

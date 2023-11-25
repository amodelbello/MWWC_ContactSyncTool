import pytest
import json


@pytest.fixture
def airtable_config_data():
    return {
        "AIRTABLE_API_KEY": "api_key",
        "AIRTABLE_BASE_ID": "base_id",
        "AIRTABLE_TABLE_ID": "table_id",
        "AIRTABLE_VIEW_ID": "view_id",
        "AIRTABLE_CHOSEN_FIRST_NAME": "first_name",
        "AIRTABLE_CHOSEN_LAST_NAME": "last_name",
        "AIRTABLE_BU_STATUS": "bu_status",
        "AIRTABLE_AREA": "area",
        "AIRTABLE_MIGS": "MIGS?",
        "AIRTABLE_STEWARD": "steward",
        "AIRTABLE_ELECTED_POSITION": "elected_position",
        "AIRTABLE_PERSONAL_EMAIL": "personal_email",
        "AIRTABLE_GOOGLE_WRITE_PERMISSIONS": "write_permissions",
        "AIRTABLE_NON_BU_ASSOCIATE": "non_bu_associate",
        # "AIRTABLE_BACKUP_DIR": "backup_dir"
    }


@pytest.fixture
def airtable_data():
    return [
        {
            "createdTime": "2023-06-10T19:20:06.000Z",
            "fields": {
                "Area": "Santa Fe LLC",
                "BU Status": "Current",
                "Chosen First Name": "aaaaa",
                "Chosen Last Name": "bbbbb",
                "MIGS?": "Yes",
                "Personal Email": "aaa@bbb.com",
            },
            "id": "recGlxjOhq8dFY9Po",
        },
        {
            "createdTime": "2022-10-03T21:57:03.000Z",
            "fields": {
                "Area": "Santa Fe INC",
                "BU Status": "Current",
                "Chosen First Name": "ccccc",
                "Chosen Last Name": "dddddd",
                "MIGS?": "Yes",
                "Personal Email": "cccc@ddddd.com",
            },
            "id": "recidq5HGk7dLWNoB",
        },
        {
            "createdTime": "2023-06-06T00:07:57.000Z",
            "fields": {
                "Area": "Denver LLC General",
                "BU Status": "Current",
                "Chosen First Name": "eeeeee",
                "Chosen Last Name": "ffffff",
                "MIGS?": "No",
                "Personal Email": "eeee@ffff.com",
            },
            "id": "recb8yqhq5wUfoOt6",
        },
        {
            "createdTime": "2023-06-15T05:55:00.000Z",
            "fields": {
                "Area": "Denver LLC General",
                "BU Status": "Current",
                "Chosen First Name": "gggggg",
                "Chosen Last Name": "hhhhhhh",
                "MIGS?": "Yes",
                "Personal Email": "ggggg@hhhhh.com",
            },
            "id": "recmxWtPfPbbfZN0v",
        },
    ]


@pytest.fixture
def create_airtable_files(tmp_path, airtable_data):
    def create_files(
        names="2023-10-26 01:28:03.097417.json",
        tmp_path=tmp_path,
        data=airtable_data,
    ):
        if not isinstance(names, list):
            names = [names]

        for name in names:
            file = tmp_path / name
            text = json.dumps(data)
            file.write_text(text)

    return create_files


@pytest.fixture
def airtable_data_with_deletion():
    return [
        {
            "createdTime": "2022-10-03T21:57:03.000Z",
            "fields": {
                "Area": "Santa Fe INC",
                "BU Status": "Current",
                "Chosen First Name": "ccccc",
                "Chosen Last Name": "dddddd",
                "MIGS?": "Yes",
                "Personal Email": "cccc@ddddd.com",
            },
            "id": "recidq5HGk7dLWNoB",
        },
        {
            "createdTime": "2023-06-06T00:07:57.000Z",
            "fields": {
                "Area": "Denver LLC General",
                "BU Status": "Current",
                "Chosen First Name": "eeeeee",
                "Chosen Last Name": "ffffff",
                "MIGS?": "No",
                "Personal Email": "eeee@ffff.com",
            },
            "id": "recb8yqhq5wUfoOt6",
        },
        {
            "createdTime": "2023-06-15T05:55:00.000Z",
            "fields": {
                "Area": "Denver LLC General",
                "BU Status": "Current",
                "Chosen First Name": "gggggg",
                "Chosen Last Name": "hhhhhhh",
                "MIGS?": "Yes",
                "Personal Email": "ggggg@hhhhh.com",
            },
            "id": "recmxWtPfPbbfZN0v",
        },
    ]


@pytest.fixture
def airtable_data_with_addition():
    return [
        {
            "createdTime": "2023-06-10T19:20:06.000Z",
            "fields": {
                "Area": "Santa Fe LLC",
                "BU Status": "Current",
                "Chosen First Name": "added",
                "Chosen Last Name": "added",
                "MIGS?": "Yes",
                "Personal Email": "added@bbb.com",
            },
            "id": "recGlxjOhq8dFY9Pj",
        },
        {
            "createdTime": "2023-06-10T19:20:06.000Z",
            "fields": {
                "Area": "Santa Fe LLC",
                "BU Status": "Current",
                "Chosen First Name": "aaaaa",
                "Chosen Last Name": "bbbbb",
                "MIGS?": "Yes",
                "Personal Email": "aaa@bbb.com",
            },
            "id": "recGlxjOhq8dFY9Po",
        },
        {
            "createdTime": "2022-10-03T21:57:03.000Z",
            "fields": {
                "Area": "Santa Fe INC",
                "BU Status": "Current",
                "Chosen First Name": "ccccc",
                "Chosen Last Name": "dddddd",
                "MIGS?": "Yes",
                "Personal Email": "cccc@ddddd.com",
            },
            "id": "recidq5HGk7dLWNoB",
        },
        {
            "createdTime": "2023-06-06T00:07:57.000Z",
            "fields": {
                "Area": "Denver LLC General",
                "BU Status": "Current",
                "Chosen First Name": "eeeeee",
                "Chosen Last Name": "ffffff",
                "MIGS?": "No",
                "Personal Email": "eeee@ffff.com",
            },
            "id": "recb8yqhq5wUfoOt6",
        },
        {
            "createdTime": "2023-06-15T05:55:00.000Z",
            "fields": {
                "Area": "Denver LLC General",
                "BU Status": "Current",
                "Chosen First Name": "gggggg",
                "Chosen Last Name": "hhhhhhh",
                "MIGS?": "Yes",
                "Personal Email": "ggggg@hhhhh.com",
            },
            "id": "recmxWtPfPbbfZN0v",
        },
    ]


@pytest.fixture
def airtable_data_with_change():
    return [
        {
            "createdTime": "2023-06-10T19:20:06.000Z",
            "fields": {
                "Area": "Santa Fe LLC",
                "BU Status": "Current",
                "Chosen First Name": "DIFFERENT!",
                "Chosen Last Name": "bbbbb",
                "MIGS?": "Yes",
                "Personal Email": "aaa@bbb.com",
            },
            "id": "recGlxjOhq8dFY9Po",
        },
        {
            "createdTime": "2022-10-03T21:57:03.000Z",
            "fields": {
                "Area": "Santa Fe INC",
                "BU Status": "Current",
                "Chosen First Name": "ccccc",
                "Chosen Last Name": "dddddd",
                "MIGS?": "Yes",
                "Personal Email": "cccc@ddddd.com",
            },
            "id": "recidq5HGk7dLWNoB",
        },
        {
            "createdTime": "2023-06-06T00:07:57.000Z",
            "fields": {
                "Area": "Denver LLC General",
                "BU Status": "Current",
                "Chosen First Name": "eeeeee",
                "Chosen Last Name": "ffffff",
                "MIGS?": "No",
                "Personal Email": "eeee@ffff.com",
            },
            "id": "recb8yqhq5wUfoOt6",
        },
        {
            "createdTime": "2023-06-15T05:55:00.000Z",
            "fields": {
                "Area": "Denver LLC General",
                "BU Status": "Current",
                "Chosen First Name": "gggggg",
                "Chosen Last Name": "hhhhhhh",
                "MIGS?": "Yes",
                "Personal Email": "ggggg@hhhhh.com",
            },
            "id": "recmxWtPfPbbfZN0v",
        },
    ]


@pytest.fixture
def action_network_config_data():
    return {
        "ACTION_NETWORK_API_KEY": "api_key",
        "ACTION_NETWORK_BASE_URL": "base_url",
    }


@pytest.fixture
def action_network_people():
    return {
        "_links": {
            "next": {"href": "https://actionnetwork.org/api/v2/people?page=2"},
        },
        "_embedded": {
            "osdi:people": [
                {
                    "identifiers": [
                        "action_network:3927fbe8-891c-4326-9796-4fd75503c56a"
                    ],
                    "email_addresses": [
                        {
                            "primary": True,
                            "address": "email1@email.com",
                            "status": "subscribed",
                        }
                    ],
                }
            ]
        },
    }


@pytest.fixture
def action_network_people_no_next():
    return {
        "_links": {},
        "_embedded": {
            "osdi:people": [
                {
                    "identifiers": [
                        "action_network:3927fbe8-891c-4326-9796-4fd75503c56a"
                    ],
                    "email_addresses": [
                        {
                            "primary": True,
                            "address": "email2@email.com",
                            "status": "subscribed",
                        }
                    ],
                }
            ]
        },
    }


@pytest.fixture
def action_network_people_bad_uuid():
    return {
        "_links": {},
        "_embedded": {
            "osdi:people": [
                {
                    "identifiers": [
                        "action_network:no-sir",
                    ],
                    "email_addresses": [
                        {
                            "primary": False,
                            "address": "email3@email.com",
                            "status": "subscribed",
                        }
                    ],
                }
            ]
        },
    }


@pytest.fixture
def google_groups_result():
    return [
        {
            "kind": "admin#directory#group",
            "id": "aaa96cc0179jnck",
            "etag": "\"rRlYht8CpEbfu8xGqIMitJC3eYqrDMbj691v3wQznfg/O8PadTH_AawQ7cTGfw65K1paaa\"",
            "email": "group1@meowwolfworkers.org",
            "name": "All BU",
            "directMembersCount": "171",
            "description": "",
            "adminCreated": True,
        },
        {
            "kind": "admin#directory#group",
            "id": "aaa96cc02bxx1s3",
            "etag": "\"rRlYht8CpEbfu8xGqIMitJC3eYqrDMbj691v3wQznfg/09sDqOe4m6UIELDBDD_rB-dnaaa\"",
            "email": "group2@meowwolfworkers.org",
            "name": "Members Read",
            "directMembersCount": "135",
            "description": "All members in good standing",
            "adminCreated": True,
        },
        {
            "kind": "admin#directory#group",
            "id": "aaasv4uv4bk2t4v",
            "etag": "\"rRlYht8CpEbfu8xGqIMitJC3eYqrDMbj691v3wQznfg/nhHuBxTIEgdDbgGIZviqK8Qaaaa\"",
            "email": "group3@meowwolfworkers.org",
            "name": "Denver LLC",
            "directMembersCount": "0",
            "description": "",
            "adminCreated": True,
        },
    ]


@pytest.fixture
def google_client(google_groups_result):
    class MockGoogleClient:

        @staticmethod
        def groups():
            class MockGroupsFn:
                @staticmethod
                def list(customer, maxResults, orderBy):
                    class MockListFn:
                        @staticmethod
                        def execute():
                            return {"groups": google_groups_result}
                    return MockListFn()
            return MockGroupsFn()

    return MockGoogleClient()

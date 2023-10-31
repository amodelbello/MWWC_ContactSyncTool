import pytest


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
                "Chosen First Name": "aaaa1",
                "Chosen Last Name": "bbbb1",
                "MIGS?": "Yes",
                "Personal Email": "aaa@bbb.com",
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

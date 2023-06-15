import pytest


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

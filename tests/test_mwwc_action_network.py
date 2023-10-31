from unittest.mock import patch
from mwwc_action_network import ActionNetwork


class MockGetResponse():
    def __init__(self, data):
        self.data = data

    def json(self):
        return self.data


@patch('requests.get')
def test_get_people(
        mock_get,
        action_network_config_data,
        action_network_people,
        action_network_people_no_next,
):
    mock_get.side_effect = [
        MockGetResponse(action_network_people),
        MockGetResponse(action_network_people),
        MockGetResponse(action_network_people_no_next),
    ]

    action_network = ActionNetwork(action_network_config_data)
    people = action_network.get_people()
    assert len(people) == 2


@patch('requests.get')
def test_get_people_bad_uuid(
        mock_get,
        action_network_config_data,
        action_network_people_bad_uuid,
):
    mock_get.side_effect = [
        MockGetResponse(action_network_people_bad_uuid),
    ]

    action_network = ActionNetwork(action_network_config_data)
    people = action_network.get_people({})
    assert not people

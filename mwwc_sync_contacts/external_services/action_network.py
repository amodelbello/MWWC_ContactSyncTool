import requests
import json
import uuid


def get_all_action_network_users(c):
    url = f"{c['ACTION_NETWORK_BASE_URL']}/people"
    headers = {"OSDI-API-Token": c["ACTION_NETWORK_API_KEY"]}
    results = []

    def is_valid_uuid(val):
        try:
            uuid.UUID(str(val))
            return True
        except ValueError:
            return False

    def response_has_next(response):
        return "next" in response["_links"]

    def get_primary_email_from_person(person):
        for item in person["email_addresses"]:
            if item["primary"] is True:
                return item["address"]

    def get_identifier_from_person(person):
        for item in person["identifiers"]:
            candidate = item.split(":")
            if len(candidate) == 2 and is_valid_uuid(candidate[1]):
                return candidate[1]

    def parse_response(response):
        person_list = []
        people = response["_embedded"]["osdi:people"]
        for person in people:
            email = get_primary_email_from_person(person)
            identifier = get_identifier_from_person(person)
            # We use email as the key because that's what we know in airtable
            person_list.append({email: identifier})

    def make_request(next=None):
        if len(results) > 0 and next is None:
            return results

        u = next if next is not None else url
        r = requests.get(u, headers=headers)
        # response = json.loads(r.json())
        response = r.json()
        next_url = None
        if response_has_next(response):
            next_url = response["_links"]["next"]["href"]

        results.append(parse_response(response))
        make_request(next_url)

    make_request()

    return results

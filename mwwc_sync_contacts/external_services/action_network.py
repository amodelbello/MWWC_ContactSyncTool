import requests
import uuid


class ActionNetwork:
    def __init__(self, c):
        self.url = f"{c['ACTION_NETWORK_BASE_URL']}/people"
        self.headers = {"OSDI-API-Token": c["ACTION_NETWORK_API_KEY"]}

    def get_people(self, results={}, next=None):
        if len(results) > 0 and next is None:
            return results

        u = next if next is not None else self.url
        r = requests.get(u, headers=self.headers)
        response = r.json()
        next_url = None
        if ActionNetwork.response_has_next(response):
            next_url = response["_links"]["next"]["href"]

        results.update(ActionNetwork.parse_response(response))
        return self.get_people(results, next_url)

    @staticmethod
    def response_has_next(response):
        return "next" in response["_links"]

    @staticmethod
    def parse_response(response):
        person_dict = {}
        people = response["_embedded"]["osdi:people"]
        for person in people:
            email = ActionNetwork.get_primary_email_from_person(person)
            identifier = ActionNetwork.get_identifier_from_person(person)
            # We use email as the key because that's what we know in airtable
            # TODO: there's a chance that a person may not have an email.
            # what should we do in that case?
            if email:
                person_dict[email] = identifier
        return person_dict

    @staticmethod
    def get_primary_email_from_person(person):
        for item in person["email_addresses"]:
            if item["primary"] is True and "address" in item:
                return item["address"]

    @staticmethod
    def get_identifier_from_person(person):
        for item in person["identifiers"]:
            candidate = item.split(":")
            if len(candidate) == 2 and ActionNetwork.is_valid_uuid(candidate[1]):
                return candidate[1]

    @staticmethod
    def is_valid_uuid(val):
        try:
            uuid.UUID(str(val))
            return True
        except ValueError:
            return False

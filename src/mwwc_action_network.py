import requests
import uuid


class ActionNetwork:
    def __init__(self, c):
        self.url = f"{c['ACTION_NETWORK_BASE_URL']}/people"
        self.headers = {"OSDI-API-Token": c["ACTION_NETWORK_API_KEY"]}

    def get_people(self, results={}, next=None):
        """
        Before we can sync contacts with action network
        we need a way to compare their data with airtable's.
        This method returns a dictionary of all action network contacts
        in { email: action_network_id} form.
        We can use this to compare with the latest airtable data to
        know which records to add and delete.
        """
        # Note the difference between using None and False here
        if next is False:
            return results

        url = next if next is not None else self.url
        r = requests.get(url, headers=self.headers)
        response = r.json()

        next_url = False
        if ActionNetwork._response_has_next(response):
            next_url = response["_links"]["next"]["href"]

        results.update(ActionNetwork._parse_response(response))

        """
        The action network api only returns paginated results.
        There is no `get_all()` method.
        This is a recursive method that keeps requesting data
        page by page until there are no more pages.
        """
        return self.get_people(results, next_url)

    @staticmethod
    def _response_has_next(response):
        return "next" in response["_links"]

    @staticmethod
    def _parse_response(response):
        person_dict = {}
        people = response["_embedded"]["osdi:people"]
        for person in people:
            email = ActionNetwork._get_primary_email_from_person(person)
            identifier = ActionNetwork._get_identifier_from_person(person)
            """
            We use email as the key because that's what we know in airtable
            TODO: there's a chance that a person may not have an email.
            what should we do in that case?
            """
            if email and identifier:
                person_dict[email] = identifier
        return person_dict

    @staticmethod
    def _get_primary_email_from_person(person):
        for item in person["email_addresses"]:
            if item["primary"] is True and "address" in item:
                return item["address"]
            else:
                return ""

    @staticmethod
    def _get_identifier_from_person(person):
        for item in person["identifiers"]:
            candidate = item.split(":")
            if len(candidate) == 2 and ActionNetwork._is_valid_uuid(candidate[1]):
                return candidate[1]
            else:
                return ""

    @staticmethod
    def _is_valid_uuid(val):
        try:
            uuid.UUID(str(val))
            return True
        except ValueError:
            return False

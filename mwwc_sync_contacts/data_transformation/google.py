def sync_google_workspace(client):
    # Call the Admin SDK Directory API
    print("Getting the first 10 users in the domain")
    results = (
        client.users()
        .list(customer="my_customer", maxResults=10, orderBy="email")
        .execute()
    )
    users = results.get("users", [])

    if not users:
        print("No users in the domain.")
    else:
        response = []
        for user in users:
            full_name = user["name"]["fullName"]
            response.append("{0} ({1})".format(user["primaryEmail"], full_name))
        return response

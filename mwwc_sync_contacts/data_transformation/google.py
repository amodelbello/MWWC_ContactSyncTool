def sync_google_workspace(client):
    members = []
    groups = []

    groups_result = (
        client.groups()
        .list(customer="my_customer", maxResults=10, orderBy="email")
        .execute()
    )
    groups = groups_result.get("groups", [])

    # list(groupKey, includeDerivedMembership=None, maxResults=None, pageToken=None, roles=None, x__xgafv=None)
    # for i, group in enumerate(groups):
    #     members_result = (
    #         client.members()
    #         .list(
    #             groupKey=group["email"],
    #             maxResults=10,
    #             # pageToken=str(i),
    #             # roles="MEMBER",
    #         )
    #         .execute()
    #     )
    #     members.append(members_result.get("members", []))
    # break
    members_result = (
        client.members()
        .list(
            groupKey="all-bu@meowwolfworkers.org",
            maxResults=200,
        )
        .execute()
    )
    members = members_result.get("members", [])

    # privs_result = (
    #     client.privileges()
    #     .list(
    #         customer="my_customer",
    #     )
    #     .execute()
    # )
    # privs = privs_result.get("items", [])

    if not members:
        print("No users in the domain.")
        # return privs
    else:
        return [groups, members]
        # response = []
        # for group in groups:
        #     full_name = group["name"]["fullName"]
        #     response.append("{0} ({1})".format(group["primaryEmail"], full_name))
        # return response

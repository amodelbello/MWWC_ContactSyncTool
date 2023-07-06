from pyairtable import Table


def get_banana_data(c):
    fields = [
        c["AIRTABLE_CHOSEN_FIRST_NAME"],
        c["AIRTABLE_CHOSEN_LAST_NAME"],
        c["AIRTABLE_BU_STATUS"],
        c["AIRTABLE_AREA"],
        c["AIRTABLE_MIGS"],
        c["AIRTABLE_STEWARD"],
        c["AIRTABLE_ELECTED_POSITION"],
        c["AIRTABLE_PERSONAL_EMAIL"],
    ]

    banana_table = Table(
        c["AIRTABLE_API_KEY"],
        c["AIRTABLE_BASE_ID"],
        c["AIRTABLE_TABLE_ID"],
    )
    return banana_table.all(view=c["AIRTABLE_VIEW_ID"], fields=fields)

from pyairtable import Table


def get_banana_data(c):
    banana_table = Table(
        c["AIRTABLE_API_KEY"],
        c["AIRTABLE_BASE_ID"],
        c["AIRTABLE_TABLE_ID"],
    )
    return banana_table.all()

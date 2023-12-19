import requests
from typing import List

from robocorp import workitems
from robocorp.tasks import task
from robocorp.workitems import ExceptionType

from RPA.HTTP import HTTP
from RPA.JSON import JSON
from RPA.Tables import Tables, Table

http = HTTP()
json = JSON()
table = Tables()

TRAFFIC_JSON_FILE_PATH = "output/traffic.json"

# JSON data keys
COUNTRY_KEY = "SpatialDim"
YEAR_KEY = "TimeDim"
RATE_KEY = "NumericValue"
GENDER_KEY = "Dim1"


@task
def produce_traffic_data():
    """
    Inhuman Insurance, Inc. Artificial Intelligence System automation.
    Produce traffic data work items.
    """
    print("produce...")
    http.download(
        url="https://github.com/robocorp/inhuman-insurance-inc/raw/main/RS_198.json",
        target_file=TRAFFIC_JSON_FILE_PATH,
        overwrite=True,
    )
    traffic_data = load_traffic_data_as_table()
    filtered_traffic_data = filter_and_sort_traffic_data(traffic_data)
    filtered_traffic_data = get_latest_data_by_country(filtered_traffic_data)
    payloads = create_work_item_payloads(filtered_traffic_data)
    save_work_item_payloads(payloads)


@task
def consume_traffic_data():
    """
    Inhuman Insurance, Inc. Artificial Intelligence System automation.
    Produce traffic data work items.
    """
    print("consume...")
    process_traffic_data()


def load_traffic_data_as_table() -> Table:
    json_data = json.load_json_from_file(TRAFFIC_JSON_FILE_PATH)
    table_from_json = table.create_table(json_data["value"])
    return table_from_json


def filter_and_sort_traffic_data(traffic_data: Table) -> Table:
    max_rate = 5.0
    both_genders = "BTSX"
    table.filter_table_by_column(traffic_data, RATE_KEY, "<", max_rate)
    table.filter_table_by_column(traffic_data, GENDER_KEY, "==", both_genders)
    table.sort_table_by_column(traffic_data, YEAR_KEY, False)
    return traffic_data


def get_latest_data_by_country(traffic_data: Table) -> list[dict | list]:
    country_key = COUNTRY_KEY
    data = table.group_table_by_column(traffic_data, country_key)
    latest_data_by_country = []
    for group in data:
        first_row = table.pop_table_row(group)
        latest_data_by_country.append(first_row)

    return latest_data_by_country


def create_work_item_payloads(traffic_data: list[dict | list]) -> List[dict]:
    payloads = []
    for row in traffic_data:
        payload = dict(
            country=row[COUNTRY_KEY],
            year=row[YEAR_KEY],
            rate=row[RATE_KEY],
        )
        payloads.append(payload)
    return payloads


def save_work_item_payloads(payloads: List[dict]):
    for payload in payloads:
        variables = dict(traffic_data=payload)
        workitems.outputs.create(variables)


def process_traffic_data():
    for item in workitems.inputs:
        traffic_data = item.payload["traffic_data"]
        if len(traffic_data["country"]) == 3:
            status, return_json = post_traffic_data_to_sales_system(traffic_data)
            if status == 200:
                item.done()
            else:
                item.fail(
                    exception_type=ExceptionType.APPLICATION,
                    code="TRAFFIC_DATA_POST_FAILED",
                    message=return_json["message"],
                )
        else:
            item.fail(
                exception_type=ExceptionType.BUSINESS,
                code="INVALID_TRAFFIC_DATA",
                message=item.payload,
            )


def post_traffic_data_to_sales_system(traffic_data: dict) -> (int, dict):
    url = "https://robocorp.com/inhuman-insurance-inc/sales-system-api"
    response = requests.post(url, json=traffic_data)
    return response.status_code, response.json()

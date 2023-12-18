from robocorp import workitems
from robocorp.tasks import task
from RPA.HTTP import HTTP
from RPA.JSON import JSON
from RPA.Tables import Tables, Table

http = HTTP()
json = JSON()
table = Tables()

TRAFFIC_JSON_FILE_PATH = "output/traffic.json"


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
    table.write_table_to_csv(filtered_traffic_data, "output/traffic.csv")


@task
def consume_traffic_data():
    """
    Inhuman Insurance, Inc. Artificial Intelligence System automation.
    Produce traffic data work items.
    """
    print("consume...")


def load_traffic_data_as_table() -> Table:
    json_data = json.load_json_from_file(TRAFFIC_JSON_FILE_PATH)
    table_from_json = table.create_table(json_data["value"])
    return table_from_json


def filter_and_sort_traffic_data(traffic_data: Table) -> Table:
    rate_key = "NumericValue"
    max_rate = 5.0
    gender_key = "Dim1"
    both_genders = "BTSX"
    year_key = "TimeDim"
    table.filter_table_by_column(traffic_data, rate_key, "<", max_rate)
    table.filter_table_by_column(traffic_data, gender_key, "==", both_genders)
    table.sort_table_by_column(traffic_data, year_key, False)
    return traffic_data

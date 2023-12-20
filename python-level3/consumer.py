import requests

from robocorp import workitems
from robocorp.tasks import task
from robocorp.workitems import ExceptionType


@task
def consume_traffic_data():
    """
    Inhuman Insurance, Inc. Artificial Intelligence System automation.
    Produce traffic data work items.
    """
    print("consume...")
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

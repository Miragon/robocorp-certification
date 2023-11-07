from RPA.Browser.Selenium import Selenium
from RPA.Excel.Files import Files
from RPA.HTTP import HTTP
from RPA.PDF import PDF

# from robocorp import browser
from robocorp.tasks import task

browser = Selenium(auto_close=False)


@task
def robot_spare_bin_python():
    """Insert the sales data for the week and export it as a PDF"""
    open_the_intranet_website()
    log_in()
    download_excel_file()
    fill_form_with_excel_data()
    collect_results()
    export_as_pdf()
    log_out()


def open_the_intranet_website():
    """Navigate to the given URL"""
    browser.open_available_browser("https://robotsparebinindustries.com/")


def log_in():
    """Fills in the login form and clicks the 'Log in' button"""
    browser.input_text("id:username", "maria")
    browser.input_text("id:password", "thoushallnotpass")
    browser.submit_form()
    browser.wait_until_page_contains_element("id:sales-form")


def fill_and_submit_sales_form(sales_rep: dict[int | str]):
    """Fills in the sales data and click the 'Submit' button"""
    browser.input_text("id:firstname", sales_rep["First Name"])
    browser.input_text("id:lastname", sales_rep["Last Name"])
    browser.select_from_list_by_value("id:salestarget", str(sales_rep["Sales Target"]))
    browser.input_text("id:salesresult", sales_rep["Sales"])
    browser.submit_form()


def download_excel_file():
    """Download Excel file from the given URL"""
    http = HTTP()
    http.download("https://robotsparebinindustries.com/SalesData.xlsx")


def fill_form_with_excel_data():
    """Read data from Excel and fill in the sales form"""
    excel = Files()
    excel.open_workbook("SalesData.xlsx")
    worksheet = excel.read_worksheet_as_table("data", header=True)
    excel.close_workbook()

    for row in worksheet:
        fill_and_submit_sales_form(row)


def collect_results():
    """Take a screenshot of the page"""
    browser.capture_element_screenshot(
        "css:div.sales-summary", "output/sales_summary.png"
    )


def export_as_pdf():
    """Export the data to a pdf file"""
    browser.wait_until_element_is_visible("id:sales-results")
    sales_results_html = browser.get_element_attribute("id:sales-results", "outerHTML")
    pdf = PDF()
    pdf.html_to_pdf(sales_results_html, "output/sales_results.pdf")


def log_out():
    """Presses the 'Log out' button"""
    browser.click_button("id:logout")
    browser.close_browser()

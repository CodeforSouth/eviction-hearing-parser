from typing import Tuple

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def load_start_page():
    driver = webdriver.Firefox()
    driver.get("https://odysseypa.traviscountytx.gov/JPPublicAccess/default.aspx")
    return driver


def load_search_page():
    start_page = load_start_page()
    try:
        element = WebDriverWait(start_page, 10).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "Civil, Family & Probate Case Records")
            )
        )
    finally:
        element.click()
        return start_page
    return None


def query_case_id(case_id: str):
    search_page = load_search_page()
    try:
        case_radio_button = WebDriverWait(search_page, 10).until(
            EC.presence_of_element_located((By.ID, "Case"))
        )
    finally:
        case_radio_button.click()

    try:
        search_box = WebDriverWait(search_page, 10).until(
            EC.presence_of_element_located((By.ID, "CaseSearchValue"))
        )
    finally:
        search_box.send_keys(case_id)
        search_button = search_page.find_element_by_name("SearchSubmit")
        search_button.click()
        search_page.implicitly_wait(1)
        return search_page
    return None

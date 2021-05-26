from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from modules import *


def selenium_dian(nit: str) -> str:
    """
    create a web driver connection and get html page with the info of nit user
    :return: a string with all html process
    """
    url = "https://muisca.dian.gov.co/WebRutMuisca/DefConsultaEstadoRUT.faces"

    with Chrome(executable_path=path_drive) as driver:
        driver.get(url)
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable(
            (By.XPATH, "//input[@name='vistaConsultaEstadoRUT:formConsultaEstadoRUT:numNit'][1]"))).send_keys(nit)
        driver.find_element_by_xpath("//*[@name='vistaConsultaEstadoRUT:formConsultaEstadoRUT:btnBuscar']").click()
        html_page = driver.page_source
    return html_page

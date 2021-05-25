#!/usr/bin/env python3
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import getcwd


def main():
    users_data = [{}]
    path_drive = f"{getcwd()}/driver/chromedriver.exe"
    url = "https://muisca.dian.gov.co/WebRutMuisca/DefConsultaEstadoRUT.faces"

    with Chrome(executable_path=path_drive) as driver:
        driver.get(url)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@name='vistaConsultaEstadoRUT:formConsultaEstadoRUT:numNit'][1]"))).send_keys(
            "11300009")
        driver.find_element_by_xpath("//*[@name='vistaConsultaEstadoRUT:formConsultaEstadoRUT:btnBuscar']").click()
        html_page = driver.page_source

    soup = BeautifulSoup(html_page, "lxml")
    nit = soup.find("input", attrs={"id": "vistaConsultaEstadoRUT:formConsultaEstadoRUT:numNit"}).get("value")
    dv = soup.find("span", attrs={"id": "vistaConsultaEstadoRUT:formConsultaEstadoRUT:dv"}).text
    primer_apellido = soup.find("span",
                                attrs={"id": "vistaConsultaEstadoRUT:formConsultaEstadoRUT:primerApellido"}).text
    segundo_apellido = ""
    primer_nombre = ""
    segundo_nombre = ""
    print(nit)
    print(dv)
    print(primer_apellido)

    # html_dian = request.urlopen(url).read().decode("utf-8")
    # soup = BeautifulSoup(html_dian, "lxml")
    # print(soup.prettify())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

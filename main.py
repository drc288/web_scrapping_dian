#!/usr/bin/env python3
from bs4 import BeautifulSoup
from modules.selenium_search import selenium_dian
from modules.dict_constrctor import dict_constructor
from sys import argv
import pandas as pd


def main():
    """
    DIAN RUT service scrapping: with the nit id, get info for people or business
    :return:
    """
    list_conversion = []
    if len(argv) != 2:
        print("Ejemplo: main.py /path/to/get/nits.csv")
        exit(1)

    df = pd.read_csv(argv[1], skip_blank_lines=True).to_dict()
    for nit in df["Nit"].values():
        html_page = selenium_dian(nit)
        list_conversion.append(dict_constructor(html_page, nit))
    print(list_conversion)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

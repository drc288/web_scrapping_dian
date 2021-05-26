from bs4 import BeautifulSoup


def dict_constructor(html: str, nit: str) -> dict:
    """
    web scraping to web page
    :param nit: nit
    :param html: html page to scrapping
    :return:
    """
    config_map = {}
    soup = BeautifulSoup(html, "lxml")
    try:
        config_map = {
            "nit": nit,
            "dv": soup.find("span", attrs={"id": "vistaConsultaEstadoRUT:formConsultaEstadoRUT:dv"}).text,
            "pa": soup.find("span", attrs={"id": "vistaConsultaEstadoRUT:formConsultaEstadoRUT:primerApellido"}).text,
            "sa": soup.find("span", attrs={"id": "vistaConsultaEstadoRUT:formConsultaEstadoRUT:segundoApellido"}).text,
            "pn": soup.find("span", attrs={"id": "vistaConsultaEstadoRUT:formConsultaEstadoRUT:primerNombre"}).text,
            "sn": soup.find("span", attrs={"id": "vistaConsultaEstadoRUT:formConsultaEstadoRUT:otrosNombres"}).text
        }
    except:
        try:
            config_map = {
                "nit": nit,
                "dv": soup.find("span", attrs={"id": "vistaConsultaEstadoRUT:formConsultaEstadoRUT:dv"}).text,
                "rz": soup.find("span", attrs={"id": "vistaConsultaEstadoRUT:formConsultaEstadoRUT:razonSocial"}).text
            }
        except Exception as err:
            config_map = {
                "nit": nit,
                "rz": "Nit no encontrado"
            }
            print(f"Se encontro un error en la extraccion de los datos, nit: {nit}\nERROR:{err}")
    return config_map

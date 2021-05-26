from os import getcwd
import platform


if platform.system() == "Linux":
    path_drive = f"{getcwd()}/driver/chromedriver"
else:
    path_drive = f"{getcwd()}/driver/chromedriver.exe"
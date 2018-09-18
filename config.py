import os
from configparser import ConfigParser

config = ConfigParser()
config.read("config.cfg", encoding="utf-8")


class SETTING:
    if os.name == 'nt':
        VERTEX_SHADER = config.get("SHADER", "VERTEX_SHADER_WIN")
        FRAGMENT_SHADER = config.get("SHADER", "FRAGMENT_SHADER_WIN")
    else:
        VERTEX_SHADER = config.get("SHADER", "VERTEX_SHADER")
        FRAGMENT_SHADER = config.get("SHADER", "FRAGMENT_SHADER")

    TITLE = config.get("SETTING_WINDOW", "TITLE")
    WIDTH_GL = int(config.get("SETTING_WINDOW", "WIDTH_GL"))
    HEIGHT_GL = int(config.get("SETTING_WINDOW", "HEIGHT_GL"))
    WIDTH_INPUT = int(config.get("SETTING_WINDOW", "WIDTH_INPUT"))
    HEIGHT_INPUT = int(config.get("SETTING_WINDOW", "HEIGHT_INPUT"))
    CAMERA_SPEED = float(config.get("CAMERA", "SPEED"))
    CAMERA_SENSITIVITY = float(config.get("CAMERA", "SENSITIVITY"))
    DELTA_TIME = int(config.get("TIMER", "DELTA"))


class STRING:
    COORD_OBSERVER = config.get("STR_INTERNATIONAL_RUS", "COORD_OBSERVER")
    LATITUDE = config.get("STR_INTERNATIONAL_RUS", "LATITUDE")
    LONGITUDE = config.get("STR_INTERNATIONAL_RUS", "LONGITUDE")

    DATE = config.get("STR_INTERNATIONAL_RUS", "DATE")
    YEAR = config.get("STR_INTERNATIONAL_RUS", "YEAR")
    MONTH = config.get("STR_INTERNATIONAL_RUS", "MONTH")
    DAY = config.get("STR_INTERNATIONAL_RUS", "DAY")
    HOUR = config.get("STR_INTERNATIONAL_RUS", "HOUR")
    MINUTE = config.get("STR_INTERNATIONAL_RUS", "MINUTE")

    CAMERA_SETTINGS = config.get("STR_INTERNATIONAL_RUS", "CAMERA_SETTINGS")
    FOV = config.get("STR_INTERNATIONAL_RUS", "FOV")
    ASPECT_RATIO = config.get("STR_INTERNATIONAL_RUS", "ASPECT_RATIO")

    ERROR_LATITUDE = config.get("STR_INTERNATIONAL_RUS", "ERROR_LATITUDE")
    ERROR_LONGITUDE = config.get("STR_INTERNATIONAL_RUS", "ERROR_LONGITUDE")

    ERROR_YEAR = config.get("STR_INTERNATIONAL_RUS", "ERROR_YEAR")
    ERROR_MONTH = config.get("STR_INTERNATIONAL_RUS", "ERROR_MONTH")
    ERROR_DAY = config.get("STR_INTERNATIONAL_RUS", "ERROR_DAY")
    ERROR_HOUR = config.get("STR_INTERNATIONAL_RUS", "ERROR_HOUR")
    ERROR_MINUTE = config.get("STR_INTERNATIONAL_RUS", "ERROR_MINUTE")

    ERROR_FOV = config.get("STR_INTERNATIONAL_RUS", "ERROR_FOV")
    ERROR_ASPECT_RATIO = config.get("STR_INTERNATIONAL_RUS", "ERROR_ASPECT_RATIO")


class RESOURCES:
    STARS_PATH = config.get("RESOURCES", "STARS_PATH")

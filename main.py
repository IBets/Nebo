import datetime
from PyQt5.QtWidgets import QApplication, QMessageBox
from x_widgets.widget_gl import GLWidget
from x_widgets.widget_input import WidgetInput
from config import STRING

__author__  = 'Mikhal Gorobets'
__version__ = '0.1'


class CheckError(Exception):
    pass


class MainWidget(WidgetInput):
    def __init__(self):
        super().__init__()
        self.button_send.clicked.connect(self.initialize)

    def initialize(self):
        try:
            self.param = {}
            self.check_error()
            self.set_param()
            self.widget_gl = GLWidget(self.param)
            self.widget_gl.show()
        except CheckError as err:
            self.show_error(err)

    def set_param(self):
        self.param["LATITUDE"] = float(self.input_coord_latitude.text())
        self.param["LONGITUDE"] = float(self.input_coord_longitude.text())
        self.param["DATETIME"] = datetime.datetime(int(self.input_date_year.text()),
                                                   int(self.input_date_month.text()),
                                                   int(self.input_date_day.text()),
                                                   int(self.input_date_hour.text()),
                                                   int(self.input_date_minute.text()))
        self.param["FOV"] = float(self.input_fov.text())
        self.param["RATIO"] = float(self.input_ratio.text())

    def show_error(self, err):
        self.msg = QMessageBox()
        text_err = ''
        for e in err.args[0]:
            text_err += (e + '\n')
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText(text_err)
        self.msg.setWindowTitle("Ошибка")
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.show()

    def check_error(self):
        self.error_str_list = []
        self._check_coord()
        self._check_error_date()
        self._check_error_camera()
        try:
            self.error_str_list[0]
        except IndexError:
            return
        else:
            raise CheckError(self.error_str_list)

    def _check_coord(self):

        if 0 <= float(self.input_coord_latitude.text()) <= 360:
            pass
        else:
            self.error_str_list.append(STRING.ERROR_LATITUDE)
        if -90 <= float(self.input_coord_longitude.text()) <= 90:
            pass
        else:
            self.error_str_list.append(STRING.ERROR_LONGITUDE)

    def _check_error_date(self):

        year = int(self.input_date_year.text())
        month = int(self.input_date_month.text())
        day = int(self.input_date_day.text())
        hour = int(self.input_date_hour.text())
        minute = int(self.input_date_minute.text())

        leap_year = False
        if year % 400 == 0:
            leap_year = True
        elif year % 100 == 0:
            leap_year = False
        elif year % 4 == 0:
            leap_year = True

        MONTH = {
            1: 31,
            2: 29 if leap_year else 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        if 1 <= year <= 9999:
            pass
        else:
            self.error_str_list.append(STRING.ERROR_YEAR)

        if 1 <= month <= 12:
            pass
        else:
            self.error_str_list.append(STRING.ERROR_MONTH)

        if 1 <= day <= MONTH.get(month, -1):
            pass
        else:
            if STRING.ERROR_MONTH in self.error_str_list:
                pass
            else:
                self.error_str_list.append(STRING.ERROR_DAY + " 1 - " + str(MONTH[month]))

        if hour < 24:
            pass
        else:
            self.error_str_list.append(STRING.ERROR_HOUR)

        if minute < 60:
            pass
        else:
            self.error_str_list.append(STRING.ERROR_MINUTE)

    def _check_error_camera(self):
        if 35 <= float(self.input_fov.text()) <= 110:
            pass
        else:
            self.error_str_list.append(STRING.ERROR_FOV)
        if 0.1 <= float(self.input_ratio.text()) <= 2:
            pass
        else:
            self.error_str_list.append(STRING.ERROR_ASPECT_RATIO)


if __name__ == '__main__':
    app = QApplication([])
    win = MainWidget()
    win.show()
    app.exec_()

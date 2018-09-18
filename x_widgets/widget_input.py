import datetime

from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QDialog
from PyQt5.QtWidgets import QFormLayout, QPushButton, QApplication
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.Qt import QRegExpValidator

from config import STRING, SETTING


class WidgetInput(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(SETTING.WIDTH_INPUT, SETTING.HEIGHT_INPUT)
        self.setWindowTitle(SETTING.TITLE)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        v_box = QVBoxLayout(self)
        data_input_layout = QFormLayout()
        data_input_layout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        data_input_layout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        data_input_layout.setFormAlignment(Qt.AlignCenter | Qt.AlignTop)
        data_input_layout.setLabelAlignment(Qt.AlignLeft)

        self.input_coord_latitude = QLineEdit()
        self.input_coord_longitude = QLineEdit()

        self.input_coord_latitude.setValidator(QRegExpValidator(QRegExp("[+-]?[0-9]+([.]?[0-9]+)?")))
        self.input_coord_longitude.setValidator(QRegExpValidator(QRegExp("[+-]?[0-9]+([.]?[0-9]+)?")))

        data_input_layout.addWidget(QLabel(STRING.COORD_OBSERVER))
        data_input_layout.addRow(STRING.LATITUDE, self.input_coord_latitude)
        data_input_layout.addRow(STRING.LONGITUDE, self.input_coord_longitude)

        self.input_date_year = QLineEdit()
        self.input_date_month = QLineEdit()
        self.input_date_day = QLineEdit()
        self.input_date_hour = QLineEdit()
        self.input_date_minute = QLineEdit()

        self.input_date_year.setValidator(QRegExpValidator(QRegExp("\d+")))
        self.input_date_month.setValidator(QRegExpValidator(QRegExp("\d+")))
        self.input_date_day.setValidator(QRegExpValidator(QRegExp("\d+")))
        self.input_date_hour.setValidator(QRegExpValidator(QRegExp("\d+")))
        self.input_date_minute.setValidator(QRegExpValidator(QRegExp("\d+")))

        data_input_layout.addWidget(QLabel(STRING.DATE))
        data_input_layout.addRow(STRING.YEAR, self.input_date_year)
        data_input_layout.addRow(STRING.MONTH, self.input_date_month)
        data_input_layout.addRow(STRING.DAY, self.input_date_day)
        data_input_layout.addRow(STRING.HOUR, self.input_date_hour)
        data_input_layout.addRow(STRING.MINUTE, self.input_date_minute)

        self.input_fov = QLineEdit()
        self.input_ratio = QLineEdit()
        self.input_fov.setValidator(QRegExpValidator(QRegExp("[0-9]+([.]?[0-9]+)?")))
        self.input_ratio.setValidator(QRegExpValidator(QRegExp("[0-9]+([.]?[0-9]+)?")))

        data_input_layout.addWidget(QLabel(STRING.CAMERA_SETTINGS))
        data_input_layout.addRow(STRING.FOV, self.input_fov)
        data_input_layout.addRow(STRING.ASPECT_RATIO, self.input_ratio)

        v_box.addLayout(data_input_layout)

        self.button_send = QPushButton("Ok")
        self.button_send.setMaximumWidth(150)

        h_box = QHBoxLayout()
        h_box.addWidget(self.button_send)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.set_default_input()

    def set_default_input(self):
        self.input_coord_latitude.setText("0")
        self.input_coord_longitude.setText("0")

        date_time = datetime.datetime(1, 1, 1).today()
        self.input_date_year.setText(str(date_time.year))
        self.input_date_month.setText(str(date_time.month))
        self.input_date_day.setText(str(date_time.day))
        self.input_date_hour.setText(str(date_time.hour))
        self.input_date_minute.setText(str(date_time.minute))
        self.input_fov.setText(str("45"))
        self.input_ratio.setText(str("1.3"))

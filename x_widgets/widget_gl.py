import datetime
import glob
import os

from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtOpenGL import QGLWidget, QGLFormat

from config import SETTING, RESOURCES
from x_buffer.buf_color import BufferColor
from x_buffer.buf_position import BufferPosition
from x_buffer.buf_size import BufferSize
from x_camera.camera import Camera
from x_math.constant_tools import hms_to_rad, sgms_to_rad, sec_to_deg, sec_to_day
from x_math.vector import Spherical
from x_pareser.parser_stars import ReaderBrightStars
from x_render.render import Render


class GLWidget(QGLWidget):
    def __init__(self, param):
        if os.name == 'nt':
            gl_format = QGLFormat()
            gl_format.setVersion(3, 3)
            gl_format.setProfile(QGLFormat.CoreProfile)
            gl_format.setSampleBuffers(True)
            super().__init__(gl_format)
        else:
            super().__init__()

        self.setWindowTitle(SETTING.TITLE)
        self.resize(SETTING.WIDTH_GL, SETTING.HEIGHT_GL)
        self.startTimer(SETTING.DELTA_TIME)
        self.key = {Qt.Key_W: False,
                    Qt.Key_S: False,
                    Qt.Key_A: False,
                    Qt.Key_D: False}

        self.mouse_press_flag = False
        self.last_pos_mouse = QPointF(0, 0)

        DEFAULT_DATE = datetime.datetime(2000, 1, 1, 0, 0)
        self.delta_time = sec_to_day((param["DATETIME"] - DEFAULT_DATE).total_seconds())
        self.camera = Camera(param["LATITUDE"], 0.0, param["LONGITUDE"])
        self.camera.perspective(param["FOV"], param["RATIO"], 0.01, 100)

    def initializeGL(self):

        self.render = Render()
        self.render.create_shader_program(SETTING.VERTEX_SHADER,
                                          SETTING.FRAGMENT_SHADER,
                                          "BASIC")

        buf_pos = BufferPosition()
        buf_size = BufferSize()
        buf_color = BufferColor()

        self._init_buf_equtor(buf_pos, buf_color, buf_size)

        self.render.create_VBO("POS")
        self.render.create_VBO("COLOR")
        self.render.create_VBO("SIZE")

        self.render.load_VBO("POS", buf_pos.data, 3)
        self.render.load_VBO("COLOR", buf_color.data, 3)
        self.render.load_VBO("SIZE", buf_size.data, 1)

        self.render.create_VAO("MAIN")
        self.render.bind_VBO("MAIN", "POS")
        self.render.bind_VBO("MAIN", "COLOR")
        self.render.bind_VBO("MAIN", "SIZE")

        self.render.bind_VAO("MAIN")
        self.render.activate_shader("BASIC")

    def paintGL(self):

        self.render.clear(0.0, 0.0, 0.0)
        mvp = self.camera.view_proect()
        self.render.shader("BASIC").set_uniform_m4("u_MVP", mvp)
        self.render.draw(self.render.size_VBO("POS"))
        self.swapBuffers()

    def resizeGL(self, width, height):
        self.render.viewport(width, height)

    def _init_buf_equtor(self, buf_pos, buf_color, buf_size):

        COLOR_TABLE = {
            "O": (0.2, 0.2, 1),
            "B": (0.5, 0.5, 1),
            "A": (1, 1, 1),
            "F": (1, 1, 0.5),
            "G": (1, 1, 0),
            "K": (1, 0.5, 0.2),
            "M": (1, 0.3, 0.2),
            "S": (1, 0.5, 0.5),
            "C": (1, 0, 0)
        }

        delta_date = self.delta_time
        cur_dir = os.path.abspath(os.path.curdir)
        os.chdir(RESOURCES.STARS_PATH)
        for file in glob.glob("*.txt"):
            with open(file, 'r') as f:
                for str_e in f.readlines():
                    star = ReaderBrightStars(str_e).read()

                    a = hms_to_rad(*star.alf_coord)
                    d = sgms_to_rad(*star.del_coord)

                    delta_a = sec_to_deg(star.n_alf) * delta_date
                    delta_d = sec_to_deg(star.n_del) * delta_date
                    a += delta_a
                    d += delta_d

                    size = 150 / (star.m * star.m)
                    if size > 30:
                        size = 30
                    if size < 1:
                        size = 1

                    buf_pos.add(Spherical(1.0, a, d).to_Vec3())
                    buf_size.add(size)
                    buf_color.add(*COLOR_TABLE[star.sp[0]])
        os.chdir(cur_dir)

    def move_camera(self):

        if self.key[Qt.Key_W]:
            self.camera.move(0.0, 0.0, -SETTING.CAMERA_SPEED)

        if self.key[Qt.Key_S]:
            self.camera.move(0.0, 0.0, SETTING.CAMERA_SPEED)

        if self.key[Qt.Key_A]:
            self.camera.move(-SETTING.CAMERA_SPEED, 0.0, 0.0)

        if self.key[Qt.Key_D]:
            self.camera.move(SETTING.CAMERA_SPEED, 0.0, 0.0)

    def timerEvent(self, *args, **kwargs):
        self.move_camera()
        self.paintGL()

    def keyPressEvent(self, event):

        if event.nativeVirtualKey() in self.key:
            self.key[event.nativeVirtualKey()] = True
		
        if event.key() in self.key:
            self.key[event.key()] = True



    def keyReleaseEvent(self, event):

        if event.nativeVirtualKey() in self.key:
            self.key[event.nativeVirtualKey()] = False
        
        if event.key() in self.key:
            self.key[event.key()] = False

    def mousePressEvent(self, event):
        self.mouse_press_flag = True

    def mouseReleaseEvent(self, event):
        self.mouse_press_flag = False

    def mouseMoveEvent(self, event):
        if self.mouse_press_flag:
            delta = event.localPos() - self.last_pos_mouse
            self.last_pos_mouse = event.localPos()
            if delta.manhattanLength() < 200:
                self.camera.rotate(delta.x() / SETTING.CAMERA_SENSITIVITY,
                                   0.0,
                                   delta.y() / SETTING.CAMERA_SENSITIVITY)

    def mouseDoubleClickEvent(self, event):
        self.setFocus()

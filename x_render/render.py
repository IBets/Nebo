from OpenGL.GL import *
from x_render.glseprogram import GLSEProgramError, GLSEProgram
from x_render.vbo import VBO
from x_render.ebo import EBO
from x_render.vao import VAO


class RenderError(Exception):
    pass


class Render:
    def __init__(self):
        self._shader_program = dict()
        self._vbo = dict()
        self._vao = dict()
        self._ebo = dict()
        glEnable(GL_PROGRAM_POINT_SIZE)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def create_shader_program(self, file_vert, file_frag, id):

        self._shader_program[id] = GLSEProgram()
        try:
            self._shader_program[id].compile_shader(file_vert)
            self._shader_program[id].compile_shader(file_frag)
            self._shader_program[id].link()
            self._shader_program[id].validate()

        except GLSEProgramError as err_glse:
            raise RenderError(err_glse)

    def size_VBO(self, id):

        try:
            return self._vbo[id].count
        except KeyError:
            raise RenderError("Key error from vbo id", id)

    def shader(self, id):
        try:
            return self._shader_program[id]
        except KeyError:
            raise RenderError("Key error shader_program id", id)

    def activate_shader(self, id):
        self._shader_program[id].use()

    def clear(self, r, g, b):
        glClearColor(r, g, b, 0.0)
        glClear(GL_COLOR_BUFFER_BIT)

    def create_VAO(self, id):
        self._vao[id] = VAO()

    def create_VBO(self, id):
        self._vbo[id] = VBO()

    def create_EBO(self, id):
        self._ebo[id] = EBO()

    def load_VBO(self, id, data, offset):
        self._vbo[id].load(data, offset)

    def load_EBO(self, id, data):
        self._ebo[id].load(data)

    def bind_VBO(self, id_vao, id_vbo):
        self._vao[id_vao].bind_VBO(self._vbo[id_vbo])

    def bind_VAO(self, id):
        self._vao[id].bind()

    def unbind_VAO(self, id):
        self._vao[id].unbind()

    def viewport(self, width, height):
        glViewport(0, 0, width, height)

    def draw(self, count_vertex):
        glDrawArrays(GL_POINTS, 0, count_vertex)

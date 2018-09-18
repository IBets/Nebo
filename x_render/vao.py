from OpenGL.GL import *


class VAO:
    def __init__(self):
        self.vao = glGenVertexArrays(1)
        self.index = 0

    def bind_VBO(self, buf):
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, buf.vbo)
        glEnableVertexAttribArray(self.index)
        glVertexAttribPointer(self.index, buf.offset, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        self.index += 1
        glBindVertexArray(0)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def bind_EBO(self, buf):
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, buf.ebo)
        glBindVertexArray(0)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    def bind(self):
        glBindVertexArray(self.vao)

    def unbind(self):
        glBindVertexArray(0)

from OpenGL.GL import *

import numpy as np


class VBO:
    def __init__(self):
        self.vbo = glGenBuffers(1)

    def load(self, vertex, offset):
        self.offset = offset
        self.count = len(vertex)
        verticles = np.array(vertex, dtype=np.float32)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER,
                     verticles.nbytes,
                     verticles,
                     GL_STATIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

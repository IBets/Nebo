import numpy as np
from OpenGL.GL import *


class EBO:
    def __init__(self):
        self.ebo = glGenBuffers(1)

    def load(self, element):
        element = np.array(element, dtype=np.uint32)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER,
                     element.nbytes,
                     element,
                     GL_STATIC_DRAW)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

from PIL       import Image
from OpenGL.GL import *

import numpy as np


class Texture:
    def __init__(self, file_name):
        self.id = None
        self.path = file_name
        im = Image.open(file_name, 'r')
        im = im.transpose(Image.FLIP_TOP_BOTTOM)
        
        width, height, data = im.size[0], im.size[1], np.array(list(im.getdata()), dtype=np.uint8)

        self.id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0,GL_RGB, width, height, 0,
                     GL_RGB,GL_UNSIGNED_BYTE, data)

        glBindTexture(GL_TEXTURE_2D, 0)

    def setup(self, shader_program, name, index):
        glActiveTexture(GL_TEXTURE0 + index)
        glBindTexture(GL_TEXTURE_2D, self.id)
        shader_program.set_uniform_i(name, index)

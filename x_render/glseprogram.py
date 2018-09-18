from OpenGL.GL import *


GLSL_SHADER = {
    'VERTEX': GL_VERTEX_SHADER,
    'FRAGMENT': GL_FRAGMENT_SHADER,
    'GEOMETRY': GL_GEOMETRY_SHADER,
    'TESS_CONTROL': GL_TESS_CONTROL_SHADER,
    'TESS_EVALUATION': GL_TESS_EVALUATION_SHADER,
    'COMPUTE': GL_COMPUTE_SHADER}

SHADER_FILE_EXTENSION = {
    "vs": GLSL_SHADER['VERTEX'],
    "vert": GLSL_SHADER['VERTEX'],
    "gs": GLSL_SHADER['GEOMETRY'],
    "geom": GLSL_SHADER['GEOMETRY'],
    "tcs": GLSL_SHADER['TESS_CONTROL'],
    "tes": GLSL_SHADER['TESS_EVALUATION'],
    "fs": GLSL_SHADER['FRAGMENT'],
    "frag": GLSL_SHADER['FRAGMENT'],
    "cs": GLSL_SHADER['COMPUTE']}

GLSE_TYPE_STRING = {
    GL_FLOAT: "float",
    GL_FLOAT_VEC2: "vec2",
    GL_FLOAT_VEC3: "vec3",
    GL_FLOAT_VEC4: "vec4",
    GL_DOUBLE: "double",
    GL_INT: "int",
    GL_UNSIGNED_INT: "unsigned int",
    GL_BOOL: "bool",
    GL_FLOAT_MAT2: "mat2",
    GL_FLOAT_MAT3: "mat3",
    GL_FLOAT_MAT4: "mat4", }


class GLSEProgramError(Exception):
    pass


class GLSEProgram:
    def __init__(self):
        self._handle = 0
        self._linked = False
        self._uniform_location = {}

    def _get_uniform_location(self, name):

        return glGetUniformLocation(self._handle, name)

    def compile_shader(self, file_name):

        open(file_name, "r")
        global type_shader
        with open(file_name, 'r') as f:
            if self._handle <= 0:
                self._handle = glCreateProgram()
                if self._handle is None:
                    raise GLSEProgramError("ERROR CREATING SHADER PROGRAM.")
            if self._handle == 0:
                raise GLSEProgramError("UNABLE TO CREATE SHADER PROGRAM.")
            try:
                type_shader = SHADER_FILE_EXTENSION[file_name.split('.')[-1]]
            except KeyError:
                raise GLSEProgramError("NOT FOUND SHADER TYPE: {}".format(type_shader))
            self._compile_shader_from_string(f.read(), type_shader)

    def _compile_shader_from_string(self, source, type_shader):

        shader_handle = glCreateShader(type_shader)
        if shader_handle is None:
            raise GLSEProgramError("ERROR CREATING SHADER TYPE: {}".format(type_shader))

        glShaderSource(shader_handle, source)
        glCompileShader(shader_handle)

        if glGetShaderiv(shader_handle, GL_COMPILE_STATUS) != GL_TRUE:
            info_log = glGetShaderInfoLog(shader_handle)
            raise GLSEProgramError("ERROR: SHADER {} \n{}".format(type_shader, info_log.decode()))
        glAttachShader(self._handle, shader_handle)

    def link(self):

        if self._linked:
            return
        if self._handle <= 0:
            raise GLSEProgramError("PROGRAM HAS NOT BEEN COMPILED.")
        glLinkProgram(self._handle)
        if glGetProgramiv(self._handle, GL_LINK_STATUS) != GL_TRUE:
            info_log = glGetProgramInfoLog(self._handle)
            raise GLSEProgramError("ERROR::SHADER::PROGRAM::LINKING_FAILED \n", info_log.decode())
        self._linked = True
        self._uniform_location.clear()

    def validate(self):

        if not self.is_linked():
            raise GLSEProgramError("PROGRAM IS NOT LINKED.")
        glValidateProgram(self._handle)
        if glGetProgramiv(self._handle, GL_VALIDATE_STATUS) != GL_TRUE:
            info_log = glGetProgramInfoLog(self._handle)
            raise GLSEProgramError("INVALID SHADER PROGRAM: ".format(info_log.decode()))

    def use(self):

        if self._handle <= 0 or (not self._linked):
            raise GLSEProgramError("SHADER HAS NOT BEEN LINKED")
        glUseProgram(self._handle)

    def get_handle(self):

        return self._handle

    def is_linked(self):

        return self._linked

    def bind_attrib_location(self, location, name):

        glBindAttribLocation(self._handle, location, name)

    def set_uniform_xyz(self, name, x, y, z):

        loc = self._get_uniform_location(name)
        glUniform3f(loc, x, y, z)

    def set_uniform_v3(self, name, vec3):

        loc = self._get_uniform_location(name)
        glUniform3f(loc, vec3.x, vec3.y, vec3.z)

    def set_uniform_v4(self, name, vec4):

        loc = self._get_uniform_location(name)
        glUniform4f(loc, vec4.x, vec4.y, vec4.z, vec4.w)

    def set_uniform_m4(self, name, mat4):

        loc = self._get_uniform_location(name)
        glUniformMatrix4fv(loc, 1, GL_TRUE, mat4.get_data())

    def set_uniform_i(self, name, ival):

        loc = self._get_uniform_location(name)
        glUniform1i(loc, ival)

    def get_type_str(self, type_GL):
        try:
            GLSE_TYPE_STRING[type_GL]
        except KeyError:
            return "?"
        else:
            return GLSE_TYPE_STRING[type_GL]

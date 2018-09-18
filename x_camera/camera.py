from x_math.angles import Angles
from x_math.matrix import Mat4
from x_math.transform import Transform
from x_math.vector import Vec3


class Camera:
    def __init__(self, pitch, yaw, roll):
        self.position = Vec3(0, 0, 0)
        self.rotation = Angles(pitch, 0.0, roll)

        self.proection = Mat4([1.0, 0.0, 0.0, 0.0],
                              [0.0, 1.0, 0.0, 0.0],
                              [0.0, 0.0, 1.0, 0.0],
                              [0.0, 0.0, 0.0, 1.0])
        rot_x = Angles(-90.0, 0.0, 0.0).to_Mat4()
        rot_y = Angles(0.0, -90.0, 0.0).to_Mat4()

        self.mat_gl_to_phys = rot_y * rot_x

    def perspective(self, fov, aspect, z_near, z_far):
        self.proection = Transform.perspective(fov, aspect, z_near, z_far)

    def ortho(self, left, right, bottom, top, z_near, z_far):
        self.proection = Transform.ortho(left, right, bottom, top, z_near, z_far)

    def move(self, x, y, z):
        move = (self.rotation.to_Mat3().transponse()) * Vec3(x, y, z)
        self.position += move

    def rotate(self, x, y, z):
        self.rotation += Angles(x, y, z)

    def view_proect(self):
        trans = Transform.translate(-self.position)
        rot = self.rotation.to_Mat4()
        proect = self.proection
        return proect * rot * trans * self.mat_gl_to_phys

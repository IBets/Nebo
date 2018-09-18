from x_math.matrix import Mat3, Mat4
from x_math.vector import Vec3, Vec4, Spherical
from x_math.angles import Angles
from x_math.constant_tools import PI
from unittest import TestCase

DELTA_FLOAT = 0.00001


class TestVec3(TestCase):
    def test_add(self):
        v_add = Vec3(0, 0, 0) + Vec3(1, 2, 3)
        self.assertAlmostEqual(v_add.x, 1, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_add.y, 2, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_add.z, 3, delta=DELTA_FLOAT)

    def test_sub(self):
        v_sub = Vec3(0, 0, 0) - Vec3(1, 2, 3)
        self.assertAlmostEqual(v_sub.x, -1, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_sub.y, -2, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_sub.z, -3, delta=DELTA_FLOAT)

    def test_mul(self):
        v_mul = Vec3(1, 2, 3) * 5
        self.assertAlmostEqual(v_mul.x, 5, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_mul.y, 10, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_mul.z, 15, delta=DELTA_FLOAT)

        v_mul = 5 * Vec3(1, 2, 3)
        self.assertAlmostEqual(v_mul.x, 5, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_mul.y, 10, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_mul.z, 15, delta=DELTA_FLOAT)

    def test_dot(self):
        dot_result = Vec3(1, 2, 3).dot(Vec3(1, 2, 3))
        self.assertAlmostEqual(dot_result, 14, delta=DELTA_FLOAT)

    def test_div(self):
        v_mul = Vec3(15.0, 10.0, 5.0) / 5.0
        self.assertAlmostEqual(v_mul.x, 3, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_mul.y, 2, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_mul.z, 1, delta=DELTA_FLOAT)


class TestVec4(TestCase):
    def test_add(self):
        v_add = Vec4(0, 0, 0, 0) + Vec4(1, 2, 3, 4)
        self.assertAlmostEqual(v_add.x, 1, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_add.y, 2, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_add.z, 3, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_add.w, 4, delta=DELTA_FLOAT)

    def test_sub(self):
        v_sub = Vec4(0, 0, 0, 0) - Vec4(1, 2, 3, 4)
        self.assertAlmostEqual(v_sub.x, -1, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_sub.y, -2, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_sub.z, -3, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_sub.w, -4, delta=DELTA_FLOAT)

    def test_mul(self):
        v_mul = Vec4(1, 2, 3, 4) * 5
        self.assertAlmostEqual(v_mul.x, 5, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_mul.y, 10, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_mul.z, 15, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_mul.w, 20, delta=DELTA_FLOAT)

        v_mul = 5 * Vec4(1, 2, 3, 4)
        self.assertAlmostEqual(v_mul.x, 5, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_mul.y, 10, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_mul.z, 15, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_mul.w, 20, delta=DELTA_FLOAT)

    def test_div(self):
        v_mul = Vec4(15.0, 10.0, 5.0, 0.0) / 5.0
        self.assertAlmostEqual(v_mul.x, 3, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_mul.y, 2, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_mul.z, 1, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_mul.w, 0, delta=DELTA_FLOAT)

    def test_dot(self):
        dot_result = Vec4(1, 2, 3, 4).dot(Vec4(1, 2, 3, 4))
        self.assertAlmostEqual(dot_result, 30, delta=DELTA_FLOAT)


class TestSpherical(TestCase):
    def test_to_Vec3(self):
        v = Spherical(1, PI / 2, 0).to_Vec3()
        self.assertAlmostEqual(v.x, 0, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v.y, 1, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v.z, 0, delta=DELTA_FLOAT)


class TestMat3(TestCase):
    def test_add(self):
        mat_1 = Mat3([1, 1, 1], [2, 2, 2], [2, 2, 2])
        mat_2 = Mat3([1, 1, 1], [2, 2, 2], [2, 2, 2])
        mat_result = mat_1 + mat_2
        mat_comp = Mat3([2, 2, 2], [4, 4, 4], [4, 4, 4])

        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(mat_result[i][j],
                                       mat_comp[i][j],
                                       delta=DELTA_FLOAT)

    def test_sub(self):
        mat_1 = Mat3([1, 1, 1], [2, 2, 2], [2, 2, 2])
        mat_2 = Mat3([1, 1, 1], [2, 2, 2], [2, 2, 2])
        mat_result = mat_1 - mat_2
        mat_comp = Mat3([0, 0, 0], [0, 0, 0], [0, 0, 0])
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(mat_result[i][j],
                                       mat_comp[i][j],
                                       delta=DELTA_FLOAT)

    def test_mul(self):
        mat_1 = Mat3([1, 1, 1], [2, 2, 2], [2, 2, 2])
        mat_2 = Mat3([1, 1, 1], [2, 2, 2], [2, 2, 2])
        mat_result = mat_1 * mat_2
        mat_comp = Mat3([5, 5, 5], [10, 10, 10], [10, 10, 10])

        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(mat_result[i][j],
                                       mat_comp[i][j],
                                       delta=DELTA_FLOAT)

        vec_res = Mat3([1, 1, 1], [2, 2, 2], [2, 2, 2]) * Vec3(1, 1, 1)
        vec_comp = Vec3(3, 6, 6)

        self.assertAlmostEqual(vec_res.x, vec_comp.x, delta=DELTA_FLOAT)
        self.assertAlmostEqual(vec_res.y, vec_comp.y, delta=DELTA_FLOAT)
        self.assertAlmostEqual(vec_res.z, vec_comp.z, delta=DELTA_FLOAT)


class TestMat4(TestCase):
    def test_add(self):
        mat_1 = Mat4([1, 1, 1, 1],
                     [2, 2, 2, 2],
                     [2, 2, 2, 2],
                     [3, 3, 3, 3])
        mat_2 = Mat4([1, 1, 1, 1],
                     [2, 2, 2, 2],
                     [2, 2, 2, 2],
                     [3, 3, 3, 3])

        mat_result = mat_1 + mat_2
        mat_comp = Mat4([2, 2, 2, 2],
                        [4, 4, 4, 4],
                        [4, 4, 4, 4],
                        [6, 6, 6, 6])

        for i in range(4):
            for j in range(4):
                self.assertAlmostEqual(mat_result[i][j],
                                       mat_comp[i][j],
                                       delta=DELTA_FLOAT)

    def test_sub(self):
        mat_1 = Mat4([1, 1, 1, 1],
                     [2, 2, 2, 2],
                     [2, 2, 2, 2],
                     [3, 3, 3, 3])
        mat_2 = Mat4([1, 1, 1, 1],
                     [2, 2, 2, 2],
                     [2, 2, 2, 2],
                     [3, 3, 3, 3])

        mat_result = mat_1 - mat_2
        mat_comp = Mat4([0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0])

        for i in range(4):
            for j in range(4):
                self.assertAlmostEqual(mat_result[i][j],
                                       mat_comp[i][j],
                                       delta=DELTA_FLOAT)

    def test_mul(self):
        mat_1 = Mat4([1, 1, 1, 1],
                     [2, 2, 2, 2],
                     [2, 2, 2, 2],
                     [3, 3, 3, 3])
        mat_2 = Mat4([1, 1, 1, 1],
                     [2, 2, 2, 2],
                     [2, 2, 2, 2],
                     [3, 3, 3, 3])

        mat_result = mat_1 * mat_2
        mat_comp = Mat4([8, 8, 8, 8],
                        [16, 16, 16, 16],
                        [16, 16, 16, 16],
                        [24, 24, 24, 24])

        for i in range(4):
            for j in range(4):
                self.assertAlmostEqual(mat_result[i][j],
                                       mat_comp[i][j],
                                       delta=DELTA_FLOAT)

        vec_res = Mat4([1, 1, 1, 1],
                       [2, 2, 2, 2],
                       [2, 2, 2, 2],
                       [3, 3, 3, 3]) * Vec4(1, 1, 1, 1)

        vec_comp = Vec4(4, 8, 8, 12)
        self.assertAlmostEqual(vec_res.x, vec_comp.x, delta=DELTA_FLOAT)
        self.assertAlmostEqual(vec_res.y, vec_comp.y, delta=DELTA_FLOAT)
        self.assertAlmostEqual(vec_res.z, vec_comp.z, delta=DELTA_FLOAT)
        self.assertAlmostEqual(vec_res.w, vec_comp.w, delta=DELTA_FLOAT)


class TestAngles(TestCase):
    def test_add(self):
        v_add = Angles(0, 0, 0) + Angles(1, 2, 3)
        self.assertAlmostEqual(v_add.pitch, 1, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_add.yaw, 2, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_add.roll, 3, delta=DELTA_FLOAT)

    def test_sub(self):
        v_add = Angles(0, 0, 0) - Angles(1, 2, 3)
        self.assertAlmostEqual(v_add.pitch, -1, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_add.yaw, -2, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_add.roll, -3, delta=DELTA_FLOAT)

    def test_mul(self):
        v_add = Angles(0, 0, 0) * 3
        self.assertAlmostEqual(v_add.pitch, 0, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_add.yaw, 0, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_add.roll, 0, delta=DELTA_FLOAT)

        v_add = 2 * Angles(1, 2, 3)
        self.assertAlmostEqual(v_add.pitch, 2, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_add.yaw, 4, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_add.roll, 6, delta=DELTA_FLOAT)

    def test_div(self):
        v_add = Angles(3, 6, 9) / 3
        self.assertAlmostEqual(v_add.pitch, 1, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_add.yaw, 2, delta=DELTA_FLOAT)
        self.assertAlmostEqual(v_add.roll, 3, delta=DELTA_FLOAT)



from x_test.test_parser  import TestParser
from x_test.test_math import TestVec3, TestVec4, TestMat3, TestMat4, TestSpherical, TestAngles

from test import  support

if __name__ == '__main__':
    support.run_unittest(TestParser,
                         TestVec3,
                         TestVec4,
                         TestMat3,
                         TestMat4,
                         TestSpherical,
                         TestAngles)



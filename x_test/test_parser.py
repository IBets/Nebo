from x_pareser.parser_stars import ReaderBrightStars
from unittest import TestCase

DELTA_FLOAT = 0.00001
class TestParser(TestCase):
    def test_parser(self):
        expr = '255 21:21: 4.3 - 4:33:36  47.47 -35.11    5.87  gG7                 -0.012 +0.011    71 -006 203222  16'
        star = ReaderBrightStars(expr)
        star.read()
        self.assertAlmostEqual(star.map, 255, delta=DELTA_FLOAT)
        self.assertTupleEqual(star.alf_coord, (21, 21, 4.3))
        self.assertTupleEqual(star.del_coord, ('-', 4, 33, 36))
        self.assertAlmostEqual(star.l_coord, 47.47, delta=DELTA_FLOAT)
        self.assertAlmostEqual(star.b_coord, -35.11, delta=DELTA_FLOAT)
        self.assertAlmostEqual(star.m, 5.87)
        self.assertEqual(star.sp, "G7")
        self.assertAlmostEqual(star.n_alf, -0.012, delta=DELTA_FLOAT)
        self.assertAlmostEqual(star.n_del, 0.011, delta=DELTA_FLOAT)



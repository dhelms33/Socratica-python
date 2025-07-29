import unnittest
from 07_circles import calc_area
class TestsCircleArea(unnittest.TestCase):
    def test_area(self):
        #test areas when raidus >= 0
        self.assertAlmostEqual(calc_area(1), pi)
        self.assertAlmostEqual(calc_area(0), 0)
        self.assertAlmostEqual(calc_area(2.1), pi* 2.1**2)
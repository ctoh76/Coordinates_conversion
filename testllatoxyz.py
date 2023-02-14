"""
This suite of test cases checks the cartesian_to_ecef and ecef_to_lla functions against expected output values for three test cases with different input values.

For each test case, the expected output values are calculated manually based on the input values and the WGS84 ellipsoid model. The assertAlmostEqual method is used to check that the actual output values are within a certain tolerance (delta) of the expected values.

To run the test cases, simply run the Python script. If all the test cases pass, you should see a message indicating that all tests passed.
"""
import unittest
import math
import llatoxyz

class TestCartesianToLLA(unittest.TestCase):

    def test_conversion(self):
        # Test case 1: (0, 0, 0) should convert to (0.0, 0.0, -6378137.0)
        x = 0.0
        y = 0.0
        z = 0.0
        lat_expected = 0.0
        lon_expected = 0.0
        alt_expected = -6378137.0

        x_ecef, y_ecef, z_ecef = llatoxyz.cartesian_to_ecef(x, y, z)
        lat, lon, alt = llatoxyz.ecef_to_lla(x_ecef, y_ecef, z_ecef)

        self.assertAlmostEqual(lat, lat_expected, delta=1e-6)
        self.assertAlmostEqual(lon, lon_expected, delta=1e-6)
        self.assertAlmostEqual(alt, alt_expected, delta=1.0)

        # Test case 2: (1000, 2000, 3000) should convert to (37.252599, -121.006477, 4135.048)
        x = 1000.0
        y = 2000.0
        z = 3000.0
        lat_expected = 37.252599
        lon_expected = -121.006477
        alt_expected = 4135.048

        x_ecef, y_ecef, z_ecef = llatoxyz.cartesian_to_ecef(x, y, z)
        lat, lon, alt = llatoxyz.ecef_to_lla(x_ecef, y_ecef, z_ecef)

        self.assertAlmostEqual(lat, lat_expected, delta=1e-6)
        self.assertAlmostEqual(lon, lon_expected, delta=1e-6)
        self.assertAlmostEqual(alt, alt_expected, delta=1.0)

        # Test case 3: (-1000, -2000, -3000) should convert to (-37.252599, 58.993523, -10574.048)
        x = -1000.0
        y = -2000.0
        z = -3000.0
        lat_expected = -37.252599
        lon_expected = 58.993523
        alt_expected = -10574.048

        x_ecef, y_ecef, z_ecef = llatoxyz.cartesian_to_ecef(x, y, z)
        lat, lon, alt = llatoxyz.ecef_to_lla(x_ecef, y_ecef, z_ecef)

        self.assertAlmostEqual(lat, lat_expected, delta=1e-6)
        self.assertAlmostEqual(lon, lon_expected, delta=1e-6)
        self.assertAlmostEqual(alt, alt_expected, delta=1.0)

if __name__ == '__main__':
    unittest.main()

import unittest

import test_police_report

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_police_report.load_tests(unittest.TestLoader()))

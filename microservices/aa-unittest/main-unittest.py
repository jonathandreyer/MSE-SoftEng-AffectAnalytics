# -*- coding: utf-8 -*-
import unittest
import sys


if __name__ == "__main__":
    testsuite = unittest.TestLoader().discover('.')
    ret = not unittest.TextTestRunner(verbosity=2).run(testsuite).wasSuccessful()
    sys.exit(ret)

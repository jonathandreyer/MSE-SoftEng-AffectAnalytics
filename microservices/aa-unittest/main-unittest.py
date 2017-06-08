# -*- coding: utf-8 -*-
import unittest
import sys
import xmlrunner


if __name__ == "__main__":
    suite = unittest.TestLoader().discover('.')
    ret = not xmlrunner.XMLTestRunner(output='report', verbosity=2).run(suite).wasSuccessful()
    sys.exit(ret)

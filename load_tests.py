import unittest
from elementary_tasks.tests import test_suit


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(test_suit)
    unittest.TextTestRunner().run(suite)

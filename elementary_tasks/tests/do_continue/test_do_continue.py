from unittest import TestCase

from elementary_tasks import do_continue


class TestDoContinue(TestCase):
    """do_continue tests"""
    def setUp(self):
        """Set up for test"""
        print('\nSet up for [' + self.shortDescription() + ']')
        print(self)

    def tearDown(self):
        """Tear down for test"""
        print('Tear down for [' + self.shortDescription() + ']\n')

    def test_do_continue_y_lower_case(self):
        """do_continue 'y' input function test"""
        result = do_continue('y')
        self.assertTrue(result)

    def test_do_continue_y_upper_case(self):
        """do_continue 'Y' input function test"""
        result = do_continue('Y')
        self.assertTrue(result)

    def test_do_continue_yes_lower_case(self):
        """do_continue 'yes' function test"""
        result = do_continue('yes')
        self.assertTrue(result)

    def test_do_continue_yes_upper_case(self):
        """do_continue 'YES' function test"""
        result = do_continue('YES')
        self.assertTrue(result)

    def test_do_continue_yes_mixed_case(self):
        """do_continue 'Yes' function test"""
        result = do_continue('Yes')
        self.assertTrue(result)

    def test_do_continue_false_string(self):
        """do_continue 'false string' function test"""
        result = do_continue('something weird')
        self.assertFalse(result)


if __name__ == '__main__':
    TestDoContinue()

import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)


class TestComplexData(unittest.TestCase):
    def setUp(self):
        # load test data
        # self.app = App(database='fixtures/test_complex.json')
        pass

    def test_customer_count(self):
        self.assertEqual(len([1, 2, 3]), 3)


# if __name__ == '__main__':
#     unittest.main()

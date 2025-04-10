def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
#This is test.py
import unittest
from main import find_largest

class TestLargestNumber(unittest.TestCase):
    def test_largest(self):
        self.assertEqual(find_largest(10, 20, 30), 30)
        self.assertEqual(find_largest(50, 20, 10), 50)
        self.assertEqual(find_largest(-1, -5, -3), -1)
        self.assertEqual(find_largest(5, 5, 5), 5)
        self.assertEqual(find_largest(7, 9, 9), 9)

if __name__ == '__main__':
    unittest.main()

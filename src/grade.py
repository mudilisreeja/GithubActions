import unittest

def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

class TestGetGrade(unittest.TestCase):
    def test_get_grade(self):
        self.assertEqual(get_grade(95), 'A')
        self.assertEqual(get_grade(65), 'D')
        self.assertEqual(get_grade(30), 'F')
        self.assertEqual(get_grade(89), 'A')  
        self.assertEqual(get_grade(69), 'D')         

if __name__ == '__main__':
    unittest.main()

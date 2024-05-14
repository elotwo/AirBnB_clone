import unittest
from test_console import console
class testsing_console(unittest.Testcase)
    def test_greet(self):
        result = greet("John")
        self.assertEqual(result, "Hello, John")
    def greet(name):
        return "Hello, " + name

if __name__ == '__main__':
    unittest.main()

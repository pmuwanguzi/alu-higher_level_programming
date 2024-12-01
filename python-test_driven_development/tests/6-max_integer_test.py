#!/usr/bin/python3
"""
Unitests for the add_integer function
"""
import unittest
from python-test_driven_development._0-add_integer import add_integer

class TestAddInteger(unittest.TestCase):
    """Test cases for the add_integer function"""

    def test_add_integers(self):
        # Test with two integers
        self.assertEqual(add_integer(5, 3), 8)
        
    def test_add_float_and_integer(self):
        # Test with a float and an integer
        self.assertEqual(add_integer(5.5, 3), 8)
        
    def test_add_integer_and_float(self):
        # Test with an integer and a float
        self.assertEqual(add_integer(5, 3.5), 8)
        
    def test_add_two_floats(self):
        # Test with two floats
        self.assertEqual(add_integer(5.5, 3.7), 9)
        
    def test_add_default_b(self):
        # Test with only the first argument (b defaults to 98)
        self.assertEqual(add_integer(5), 103)

    def test_invalid_a_type(self):
        # Test invalid type for `a` (string)
        with self.assertRaises(TypeError):
            add_integer("string", 3)

    def test_invalid_b_type(self):
        # Test invalid type for `b` (string)
        with self.assertRaises(TypeError):
            add_integer(5, "string")
            
    def test_both_invalid(self):
        # Test invalid types for both `a` and `b`
        with self.assertRaises(TypeError):
            add_integer("string", "string")

if __name__ == "__main__":
    unittest.main()

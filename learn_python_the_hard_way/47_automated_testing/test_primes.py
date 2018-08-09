"""
Source: 
https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/

Unit testing, tests a single unit of code in isolation. A unit could be an entire moduel, a single class or function, or almost anything in between. What's important, howeer, is that the code is isolated from other code we're not testing. 

Using Python's build-in unitest framework, any member function whose name begins with test in a class deriving from unittest.TestCase will be run, and its assertions checked, when unittest.main() is called.

Why Testing?
- Testing makes sure your code works properly under a given set of conditions.
- Testing allows one to ensure that changes to the code didn't break existing functionality.
- Testing forces one to think about the code under unusual conditions, possibly revealing logical errors.
- Good testing requires modular, decoupled code, which is hallmark of good system design.
"""

import unittest
from prime import is_prime

class PrimesTestCase(unittest.TestCase):
    
    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))
    
    def test_is_four_non_prime(self):
        self.assertFalse(is_prime(4), msg="Four is not prime!")
    
    def test_is_zero_not_prime(self):
        self.assertFalse(is_prime(0))
    
    def test_negative_number(self):
        
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index), msg = f'{index} should not be determined to be prime.')
            
if __name__ == '__main__':
    unittest.main()
"""doc"""

from unittest import TestCase
import operators
import logic

class OperatorsTests(TestCase):
    """-10"""
    def test_add(self):
        self.assertEquals(operators.add(2,3), 5)
    
    def test_mul(self):
        self.assertEquals(operators.mul(2,3), 6)
        
    def test_and(self):
        self.assertEquals(logic.and_(True,True), True)
    
    def test_or(self):
        self.assertEquals(logic.or_(True,False), True)

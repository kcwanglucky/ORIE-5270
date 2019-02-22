import unittest
import detectSubnormalNumber

class TestdetectSubnormalNumber(unittest.TestCase):
	def test_isSubnormal(self):
		"""
		Not a subnormal number
		"""
		self.assertEqual(False, detectSubnormalNumber.isSubnormal(0.1))
		self.assertEqual(False, detectSubnormalNumber.isSubnormal(0))
		self.assertEqual(False, detectSubnormalNumber.isSubnormal(float('inf')))
		self.assertEqual(False, detectSubnormalNumber.isSubnormal(2**(-1022)))
		
		"""
		Is a subnormal number
		"""
		self.assertEqual(True, detectSubnormalNumber.isSubnormal(2**(-1022-50)))
		self.assertEqual(True, detectSubnormalNumber.isSubnormal(2**(-1022-49)))
		self.assertEqual(True, detectSubnormalNumber.isSubnormal(2**(-1022-52)))
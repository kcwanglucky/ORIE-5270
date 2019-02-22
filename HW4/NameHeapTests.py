import unittest
import hw4

class TestNameHeap(unittest.TestCase):
	def setUp(self):
		self.heap = hw4.NameHeap()

	def test_insertName(self):
		self.heap.insertName("Bob Ross") 
		self.heap.insertName("Bob Rass")
		self.heap.insertName("Bab Ross") 

		self.assertEqual(3, self.heap.size())

	def test_deleteSmallestName(self):
		# Use different similar name to test the order 
		self.heap.insertName("Bob Ross") 
		self.heap.insertName("Bob Rass")
		self.heap.insertName("Bab Ross") 

		# Order: Bob Rass, Bab Ross, Bob Ross
		self.assertEqual("Bob Rass", self.heap.deleteSmallestName())
		self.assertEqual("Bab Ross", self.heap.deleteSmallestName())
		self.assertEqual("Bob Ross", self.heap.deleteSmallestName())

		self.assertEqual(0, self.heap.size())

	def test_smallestName(self):
		# insert multiple similar name to test the order correctness
		self.heap.insertName("Bob Ross") 
		self.heap.insertName("Bob Rass")
		self.heap.insertName("Bab Ross") 

		# Order: Bob Rass, Bab Ross, Bob Ross
		self.assertEqual("Bob Rass", self.heap.smallestName())

	""" size() has been implicitly tested by previous test function
		Include the test_size() just to make sure it really works
	"""
	def test_size(self):
		self.assertEqual(0, self.heap.size())
		self.heap.insertName("Bob Ross") 
		self.assertEqual(1, self.heap.size())
		self.heap.deleteSmallestName()
		self.assertEqual(0, self.heap.size())
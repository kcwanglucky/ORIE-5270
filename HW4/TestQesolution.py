import unittest
import qesolution
import qesolutionRevise

class Testqesolution(unittest.TestCase):
	# Test the normal (b, c) pair (not extreme values) Q1
	def test_qeSol(self):
		b =2**10+0.4543653446748
		c = 3**5
		sol1, sol2 = qesolution.qeSol(b, c)

		th_sum = 2 * b
		real_sum = (sol1 + sol2).real
		
		#print("{:.30f}".format(th_sum))
		#print("{:.30f}".format(real_sum))
		rel_err_sum = (real_sum - th_sum)/th_sum
		#print(rel_err_sum)
		self.assertEqual(True, rel_err_sum <= 1e-12)
		
		th_multiplication = -1 * c
		real_multiplication = (sol1 * sol2).real
		#print("{:.30f}".format(th_multiplication))
		#print("{:.30f}".format(real_multiplication))
		rel_err_multiplication = (real_multiplication - th_multiplication)/th_multiplication
		#print(rel_err_multiplication)
		
		# To check that the accuracy is at least 10^-12
		self.assertEqual(True, rel_err_multiplication < 1e-12)

	# Test the normal (b, c) pair (not extreme values) Q1
	def test_qeSol1(self):
		b =2**20
		c = 3**15
		sol1, sol2 = qesolution.qeSol(b, c)

		th_sum = 2 * b
		real_sum = (sol1 + sol2).real
		
		#print("{:.30f}".format(th_sum))
		#print("{:.30f}".format(real_sum))
		rel_err_sum = (real_sum - th_sum)/th_sum
		#print(rel_err_sum)
		self.assertEqual(True, rel_err_sum <= 1e-12)
		
		th_multiplication = -1 * c
		real_multiplication = (sol1 * sol2).real
		#print("{:.30f}".format(th_multiplication))
		#print("{:.30f}".format(real_multiplication))
		rel_err_multiplication = (real_multiplication - th_multiplication)/th_multiplication
		#print(rel_err_multiplication)

		# To check that the accuracy is at least 10^-12
		self.assertEqual(True, rel_err_multiplication < 1e-12)

	# Test some extreme values Q2
	def test_qeSol2(self):
		b = 2**25 + 7 ** 4 
		c = 1.9848237598435923649562934
		sol1, sol2 = qesolution.qeSol(b, c)

		th_sum = 2 * b
		real_sum = (sol1 + sol2).real
		
		#print("{:.30f}".format(th_sum))
		#print("{:.30f}".format(real_sum))
		rel_err_sum = (real_sum - th_sum)/th_sum
		self.assertEqual(True, rel_err_sum <= 1e-12)
		
		th_multiplication = -1 * c
		real_multiplication = (sol1 * sol2).real
		#print("{:.30f}".format(th_multiplication))
		#print("{:.30f}".format(real_multiplication))
		rel_err_multiplication = (real_multiplication - th_multiplication)/th_multiplication

		# To check that the accuracy is at least 10^-12
		self.assertEqual(False, rel_err_multiplication < 1e-12)

	# Test the normal (b, c) pair (not extreme values) Q1
	def test_qeSol3(self):
		b = 245435345
		c = 1234327
		sol1, sol2 = qesolution.qeSol(b, c)

		th_sum = 2 * b
		real_sum = (sol1 + sol2).real
		
		#print("{:.30f}".format(th_sum))
		#print("{:.30f}".format(real_sum))
		rel_err_sum = (real_sum - th_sum)/th_sum
		self.assertEqual(True, rel_err_sum <= 1e-12)
		
		th_multiplication = -1 * c
		real_multiplication = (sol1 * sol2).real
		#print("{:.30f}".format(th_multiplication))
		#print("{:.30f}".format(real_multiplication))
		rel_err_multiplication = (real_multiplication - th_multiplication)/th_multiplication

		# To check that the accuracy is at least 10^-12
		self.assertEqual(True, rel_err_multiplication < 1e-12)

	# Test the normal (b, c) pair (not extreme values) Q1
	def test_qeSol3_revise(self):
		b = 2**25 + 7 ** 4 
		c = 1.9848237598435923649562934
		sol1, sol2 = qesolutionRevise.qeSol(b, c)

		th_sum = 2 * b
		real_sum = (sol1 + sol2).real
		
		rel_err_sum = (real_sum - th_sum)/th_sum
		self.assertEqual(True, rel_err_sum <= 1e-12)
		
		th_multiplication = -1 * c
		real_multiplication = (sol1 * sol2).real
		
		rel_err_multiplication = (real_multiplication - th_multiplication)/th_multiplication

		# Using the revised one pass this accuracy test, which is rejected by the original
		# quadratic formula-based roots
		self.assertEqual(True, rel_err_multiplication < 1e-12)

	# Test some extreme values Q2 with revised version qesolutionRevise
	def test_qeSol4_revise(self):
		b =2**20
		c = 3**15
		sol1, sol2 = qesolutionRevise.qeSol(b, c)

		th_sum = 2 * b
		real_sum = (sol1 + sol2).real
		
		#print("{:.30f}".format(th_sum))
		#print("{:.30f}".format(real_sum))
		rel_err_sum = (real_sum - th_sum)/th_sum
		#print(rel_err_sum)
		self.assertEqual(True, rel_err_sum <= 1e-12)
		
		th_multiplication = -1 * c
		real_multiplication = (sol1 * sol2).real
		#print("{:.30f}".format(th_multiplication))
		#print("{:.30f}".format(real_multiplication))
		rel_err_multiplication = (real_multiplication - th_multiplication)/th_multiplication
		#print(rel_err_multiplication)

		# To check that the accuracy is at least 10^-12
		self.assertEqual(True, rel_err_multiplication < 1e-12)
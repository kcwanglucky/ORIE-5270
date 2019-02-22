# Solve the quadratic equation x**2 - 2*b*x - c = 0
import cmath

def qeSol(b, c):
	# calculate the discriminant
	d = 4*(b**2) + (4*c)

	# find two solutions
	sol1 = (2*b-cmath.sqrt(d))/2
	sol2 = (2*b+cmath.sqrt(d))/2

	sol1_conj = 2*c / (-2 * b + cmath.sqrt(d))
	sol2_conj = 2*c / (-2 * b - cmath.sqrt(d))

	th_sum = 2 * b
	real_sum = (sol1 + sol2).real
	real_sum_conj = (sol1_conj + sol2_conj).real
	
	rel_err_sum = (real_sum - th_sum)/th_sum
	rel_err_sum_conj = (real_sum_conj - th_sum)/th_sum
	
	
	th_multiplication = -1 * c
	real_multiplication = (sol1 * sol2).real
	real_multiplication_conj = (sol1_conj * sol2_conj).real

	rel_err_multiplication = (real_multiplication - th_multiplication)/th_multiplication
	rel_err_multiplication_conj = (real_multiplication_conj - th_multiplication)/th_multiplication
	
	if rel_err_sum_conj < rel_err_sum and rel_err_multiplication_conj < rel_err_multiplication:
		return (sol1_conj, sol2_conj)
	else:
		return (sol1, sol2)

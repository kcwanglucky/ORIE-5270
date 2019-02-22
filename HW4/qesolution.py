# Solve the quadratic equation x**2 - 2*b*x - c = 0
import cmath

def qeSol(b, c):

	# calculate the discriminant
	d = 4*(b**2) + (4*c)

	# find two solutions
	sol1 = (2*b-cmath.sqrt(d))/2
	sol2 = (2*b+cmath.sqrt(d))/2

	return (sol1, sol2)

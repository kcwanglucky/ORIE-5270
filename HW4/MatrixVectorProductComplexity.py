# Reference: https://www.geeksforgeeks.org/python-code-for-time-complexity-plot-of-heap-sort/
import numpy as np
import time
import matplotlib.pyplot as plt

def matrixVectproduct(A, b): 
	return A*b

def ON2(n):
    temp = 0
    for i in range(n):
        temp += 1
        for j in range(n):
            temp += 1

def plotTC():
	"""
	Run timer and plot time complexity
	"""
	input_size = []
	t= []
	t_ON2 = []
	for i in range(1, 10):
		# generate some random matrix and vector with n = 1000 * i
		A = np.random.rand(1000 * i, 1000 * i)
		b = np.random.rand(1000 * i, 1)
		
		start = time.clock()
		matrixVectproduct(A, b)
		end = time.clock()

		start_ON2 = time.clock()
		ON2(1000 * i)
		end_ON2 = time.clock()

		input_size.append(1000 * i)
		t.append(end - start)
		t_ON2.append(end_ON2 - start_ON2)

	plt.title("Complexity Plot")
	plt.xlabel('Input Size') 
	plt.ylabel('Time Consumed')
	plt.plot(input_size, t, color='green', label ='Matrix Vector Product (numpy)')
	plt.plot(input_size, t_ON2, color='red', label ='Normal O(n^2) Function')
	plt.legend(loc='upper left')
    

# main() function
def main():
	plotTC()
	# show plot
	plt.savefig('complexity_plot.pdf')

# call main
if __name__ == '__main__':
	main()

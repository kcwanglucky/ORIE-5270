import threading
import math
import sys
import timeit

def add(i):
	global total

	lock.acquire()
	sumApprox = 0

	for i in range(i, i + k):
		sumApprox = sumApprox + (1 / (i ** 2))
	
	total = total + sumApprox

	lock.release()

if __name__ == '__main__':
	N = int(sys.argv[1])
	total = 0

	lock = threading.Lock()

	#start_time = timeit.default_timer()
	
	k = int(math.sqrt(N))
	numGroup = int(N / k)

	threads = []

	for i in range(numGroup):
		w = threading.Thread(target=add, args=(k * i + 1,))
		w.start()
		threads.append(w)

	for w in threads:
		w.join()

	print(math.sqrt(total * 6))
	#print(timeit.default_timer() - start_time)





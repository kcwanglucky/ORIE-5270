import threading
import math
import sys
import timeit

N = int(sys.argv[1])
sumApprox = 0

lock = threading.Lock()

def add(i):
	global sumApprox

	lock.acquire()
	
	temp = sumApprox
	
	sumApprox = temp + (1 / (i ** 2))

	lock.release()

#start_time = timeit.default_timer()
for i in range(N):
	w = threading.Thread(target=add, args=(i + 1,))
	w.start()

print(math.sqrt(sumApprox * 6))

#print(timeit.default_timer() - start_time)
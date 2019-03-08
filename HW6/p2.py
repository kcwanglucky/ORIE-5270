from mrjob.job import MRJob
from mrjob.step import MRStep		# To produce multiple layers
import numpy as np


class MRpiMCS(MRJob):  #inherit the MRJob class, only need to tell how to do map reduce
	
	def steps(self): #By default, run mapper and reducer
		return [ MRStep(mapper = self.mapper, 
						reducer = self.reducer),  # specify "this is the map to start", rather than
				 MRStep(reducer = self.reducer_est_pi)								# use the default behavior
				]
	
	def mapper(self, _, N_input):		# don't care about the key
		global N
		N = int(N_input)
		for i in range(N):
			(x, y) = np.random.uniform(0, 1, 2) 

			#take the word found in lower case, yield: a primitive, like return
			#but yield return a list of things; faster, equivalent to the following two lines
			yield None, (x, y)	
			
			# lst.append(word.lower())
			# return list
	def reducer(self, _, pairs):	# say word = bear, count = [1, 1, 1, 1, 1]
		
		for pair in pairs:
			#print(pair[0], pair[1])
			temp = (pair[0] - 0.5) ** 2 + (pair[1] - 0.5) ** 2
			if temp <= 0.25:
				ret = 1
			else:
				ret = 0
			yield None, ret			# Go to the server that handles the "None" key
		# tuple, compare first key, second key, ...

	def reducer_est_pi(self, tf, counts):
		
		counts1 = counts
		N_inner = sum(counts)
		global N

		#N = sum(1 for x in counts)
		#N = len(list(counts))
		#print(N_inner)
		#print(N)
		yield (True, 4 * N_inner / N) # Take for all and look for the maximum pair

if __name__ == '__main__':
	N = 0
	MRpiMCS.run()
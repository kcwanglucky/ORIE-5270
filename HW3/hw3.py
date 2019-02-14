class NameHeap:
	def __init__(self):
		self.num_name = 0
		self.data = []

	'''
	Adds the given name to the heap
	insertName() calls the function bubbleUp() to find the correct position for the newly added name
	Because bubbleUp() takes O(log(n)) time, this function also takes O(log(n)) time
	'''
	def insertName(self, name):
		self.data.append(name)
		self.bubbleUp(self.num_name)
		self.num_name = self.num_name + 1

	'''
	Returns the smallest name (smallest in the sense mentioned in the question) from the heap
	Just return the first entry of the array, O(1)
	'''
	def smallestName(self):
		return self.data[0]

	'''
	Removes the smallest name from the heap
	deleteSmallestName() calls the function bubbleDown() to find the correct position for the newly deleted name
	(root node). Because bubbleDown() takes O(log(n)) time, this function also takes O(log(n)) time
	'''
	def deleteSmallestName(self):
		toReturn = self.data[0]
		self.data[0] = self.data[self.num_name - 1]
		self.num_name = self.num_name - 1
		self.bubbleDown(0)
		return toReturn

	'''
	Return the size of all the name in the heap
	Directly return the class feature num_name, O(1)
	'''
	def size(self):
		return self.num_name

	'''
	Returns true if the string name occurs anywhere in the current heap
	This function loops through all the name currently in the heap, so O(n)
	'''
	def contains(self, name):				# ask how to deal with duplicate name
		doesContain = False
		for dat in self.data:
			if dat == name:
				doesContain = True
				break
		return doesContain

	''' 
	return 1 if a should occur before b, otherwise -1
	a and b should be "name" instead of index
	'''
	def compare(self, a, b):
		a_sep, b_sep = a.split(" "), b.split(" ")
		if a_sep[1] < b_sep[1]:
			return 1
		elif a_sep[1] == b_sep[1] and a_sep[0] < b_sep[0]:		#ask how to deal with duplicate name
			return 1
		else:
			return -1

	'''
	bubbleUp() finds the proper position for the name at index = "child" in the binary tree with the bottom-up
	approach. At each step it moves up one level in the binary tree if necessary, so it takes O(log(n))
	'''
	def bubbleUp(self, child):
		while child > 0:
			child_name = self.data[child]
			parent = (child - 1) // 2
			parent_name = self.data[parent]

			if self.compare(parent_name, child_name) < 0:
				self.swap(parent, child)
				child = parent
			else:
				break

	'''
	bubbleDown() finds the proper position for the name at index = "parent" in the binary tree with the top-down
	approach. At each step it moves down one level in the binary tree if necessary, so it takes O(log(n))
	'''
	def bubbleDown(self, parent):
		while parent < self.num_name:
			child = self.largerChild(parent)
			
			# already a leaf node
			if child == -1:
				return

			child_name = self.data[child]
			parent_name = self.data[parent]

			if self.compare(parent_name, child_name) < 0:
				self.swap(parent, child)
				parent = child
			else:
				break

	'''
	Return the index of the child that should be considered moving up one level
	Takes O(1) time
	'''
	def largerChild(self, index):
		left_child = 2 * index + 1
		right_child = 2 * index + 2

		if left_child > self.num_name - 1:		# leaf node, no child
			return -1
		elif left_child == self.num_name - 1:
			return left_child
		else:
			return left_child if self.compare(self.data[left_child], self.data[right_child]) > 0 else right_child

	'''
	Swap the entries indexed by a and b, O(1)
	'''
	def swap(self, a, b):
		temp = self.data[a]
		self.data[a] = self.data[b]
		self.data[b] = temp


class CallCenter:
	def __init__(self):
		self.hour = 0
		self.waitlist = []
		self.oldest_hour = 0
		self.total_waiting = 0

	'''
	queueCustomer() calls insertName() of class NameHeap, which takes O(log(n)) time
	Other operations are O(1). Hence this method is O(log(n))
	'''
	def queueCustomer(self, name):
		hour_to_add = self.hour
		if self.total_waiting == 0:
			new_hour = NameHeap()
			self.waitlist.append(new_hour)
		self.waitlist[hour_to_add].insertName(name)
		self.total_waiting = self.total_waiting + 1

	'''
	dequeueCustomer() calls deleteSmallestName() of class NameHeap, which takes O(log(n)) time
	Other operations are O(1). Hence this method is O(log(n))
	'''
	def dequeueCustomer(self):
		if self.waitlist[self.oldest_hour].size() == 0:
			self.oldest_hour = self.oldest_hour + 1
		
		customer_to_return = self.waitlist[self.oldest_hour].deleteSmallestName()
		self.total_waiting = self.total_waiting - 1
		return customer_to_return

	'''
	Only involves O(1) operations, so O(1)
	'''
	def nextHour(self):
		self.hour = self.hour + 1
		new_hour = NameHeap()
		self.waitlist.append(new_hour)

	'''
	Returns "total_waiting" feature, the number of customers currently waiting to be processed
	Takes O(1) time
	'''
	def size(self):
		return self.total_waiting

	'''
	Returns true if a customer of the given name is currently waiting, otherwise false
	This function loops through all the name currently in all the heap.
	Because there are n names in the CallCenter, so O(n)
	'''
	def contains(self, name):
		for list_each_hour in self.waitlist:
			if list_each_hour.contains(name):
				return True
		return False

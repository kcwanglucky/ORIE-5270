class NameHeap:
	def __init__(self):
		self.num_name = 0
		self.data = []

	def insertName(self, name):
		self.data.append(name)
		self.bubbleUp(self.num_name)
		self.num_name = self.num_name + 1

	def smallestName(self):
		return self.data[0]

	def deleteSmallestName(self):
		toReturn = self.data[0]
		self.data[0] = self.data[self.num_name - 1]
		self.num_name = self.num_name - 1
		self.bubbleDown(0)
		return toReturn

	def size(self):
		return self.num_name

	def contains(self, name):				# ask how to deal with duplicate name
		doesContain = False
		for dat in self.data:
			if dat == name:
				doesContain = True
				break
		return doesContain

	# return 1 if a should occur before b, otherwise -1, a and b should be "name" instead of just index
	def compare(self, a, b):
		a_sep, b_sep = a.split(" "), b.split(" ")
		if a_sep[1] < b_sep[1]:
			return 1
		elif a_sep[1] == b_sep[1] and a_sep[0] < b_sep[0]:		#ask how to deal with duplicate name
			return 1
		else:
			return -1

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

	def largerChild(self, index):
		left_child = 2 * index + 1
		right_child = 2 * index + 2

		if left_child > self.num_name - 1:		# leaf node, no child
			return -1
		elif left_child == self.num_name - 1:
			return left_child
		else:
			return left_child if self.compare(self.data[left_child], self.data[right_child]) > 0 else right_child


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

	def queueCustomer(self, name):
		hour_to_add = self.hour
		if self.total_waiting == 0:
			new_hour = NameHeap()
			self.waitlist.append(new_hour)
		self.waitlist[hour_to_add].insertName(name)
		self.total_waiting = self.total_waiting + 1

	def dequeueCustomer(self):
		if self.waitlist[self.oldest_hour].size() == 0:
			self.oldest_hour = self.oldest_hour + 1
		
		customer_to_return = self.waitlist[self.oldest_hour].deleteSmallestName()
		self.total_waiting = self.total_waiting - 1
		return customer_to_return

	def nextHour(self):
		self.hour = self.hour + 1
		new_hour = NameHeap()
		self.waitlist.append(new_hour)

	def size(self):
		return self.total_waiting

	def contains(self, name):
		for list_each_hour in self.waitlist:
			if list_each_hour.contains(name):
				return True
		return False









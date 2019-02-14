import hw3

heap = hw3.NameHeap() 
heap.deleteSmallestName()
heap.insertName("Bob Ross") 
heap.insertName("Bob Rass")
heap.insertName("Bab Ross") 
heap.insertName("Ben Grimmer") 
heap.insertName("Lijun Ding")

print(heap.size() == 5) 
print(heap.smallestName() == "Lijun Ding") 
print(heap.contains("Bob Ross"))

heap.deleteSmallestName() 
print(heap.smallestName() == "Ben Grimmer")
heap.deleteSmallestName() 
print(heap.smallestName() == "Bob Rass")
heap.deleteSmallestName() 
print(heap.smallestName() == "Bab Ross")
print(heap.size() == 2) 


callCenter = hw3.CallCenter()
callCenter.dequeueCustomer()
callCenter.queueCustomer("Bob Ross") 
callCenter.queueCustomer("Ben Grimmer") 
callCenter.nextHour()
callCenter.queueCustomer("Lijun Ding") 
callCenter.queueCustomer("Jim Renegar")
callCenter.nextHour()
callCenter.nextHour()
callCenter.queueCustomer("Lucky Wang") 

print(callCenter.size() == 4) #False
print(callCenter.dequeueCustomer()=="Ben Grimmer") 
print(callCenter.dequeueCustomer()=="Bob Ross") 
print(callCenter.dequeueCustomer()=="Lijun Ding") 
print(callCenter.contains("Jim Renegar"))
print(callCenter.size() == 1) #False
callCenter.nextHour()
callCenter.queueCustomer("Bob Ross")
print(callCenter.contains("Ben Grimmer")) # False
print(callCenter.contains("Bob Ross")) # True
print(callCenter.size() == 3) #True
print(callCenter.dequeueCustomer()=="Jim Renegar")  # True
print(callCenter.dequeueCustomer()=="Lucky Wang")  # True
print(callCenter.size() == 1) #True
print(callCenter.dequeueCustomer()=="Bob Ross") 
callCenter.dequeueCustomer()

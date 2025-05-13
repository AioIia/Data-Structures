from CircularLinkedList import *

class LinkedQueue:
	def __init__(self):
		self.queue = CircularLinkedList()

	def enqueue(self, x): # insert an element to the end of the queue
		self.queue.append(x)

	def dequeue(self): # remove an element from the front of the queue
		return self.queue.pop(0)

	def front(self): # returns the front node of the queue without deleting it
		return self.queue.get(0)

	def isEmpty(self) -> bool: # returns true if queue is empty, else false.
		return self.queue.isEmpty()

	def dequeueAll(self): # clean the queue
		self.queue.clear()

	def size(self): # clean the queue
		return self.queue.size()

	def printQueue(self): # print elements from front to end
		self.queue.printList()

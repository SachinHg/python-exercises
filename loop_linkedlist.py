class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
	def detectRemoveLoop(self):
		slow = fast = self.head
		while slow and fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				self.removeLoop(slow)
				return 1
		return 0
	def removeLoop(self,node):
		p1 = node
		p2 = node
		k = 1
		while p1.next != p2:
			p1 = p1.next
			k+=1
		p1 = self.head
		p2 = self.head
		for i in rane(k):
			p2 = p2.next
		while p2 != p1:
			p1 = p1.next
			p2 = p2.next
		p2 = p2.next
		while p2.next != p1:
			p2 = p2.next
		p2.next = None
	def push(self,new):
		node = Node(data)
		new.next = self.head
		self.head = new
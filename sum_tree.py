class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

def hasSumPath(node,S):
	if node == None:
		return False
	subSum = S - node.data
	if subSum == 0 and node.left == None and node.right == None:
		return True
	return hasSumPath(node.left,subSum) or hasSumPath(node.right,subSum)

s = 13
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
if hasSumPath(root,s):
	print("Yes")
else:
	print("No")
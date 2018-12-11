class Node:
	def __init__(self, val, left=None, right=None):
		self.val=val
		self.left=left
		self.right=right

def serialize(root):
	if(root==None):
		return "#"
	else:
		return "{} {} {}".format(root.val,serialize(root.left),serialize(root.right))

def deserialize(data):
	def helper():
		val=next(vals)
		if val =="#":
			return None
		node=Node(int(val))
		node.left=helper()
		node.right=helper()
		return node
	vals=iter(data.split())
	return helper()

data="1 2 # # 3 # #"
deserialize(data)

tree = Node(1, Node(2), Node(3))

str = serialize(tree)

print(str)
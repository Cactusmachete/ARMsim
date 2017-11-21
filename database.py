

class instruction():
	"""docstring for ClassName"""
	def __init__(self, data, type):
		super(ClassName, self).__init__()
		self.data = data;
		self.type = type;


class node():
	"""docstring for node"""
	def __init__(self, instruction):
		super(node, self).__init__()
		self.instruction = instruction;
		self.left = null;
		self.right = null;


class tree():
	"""docstring for tree"""
	def __init__(self, root):
		super(tree, self).__init__()
		self.root = root


	def addNode(self, root, node, bit_num):
		if(node.instruction.data[bit_num]=="1"):
			if(root.right==null):
				root.right = node;
			else:
				addNode(root.right, node, bit_num+1);
		else:
			if(root.left==null):
				root.right = node;
			else:
				addNode(root.left, node, bit_num+1);

	def find(self, root, string):
		#returns object of type instruction
		if((root.right==null and root.left==null) or string.length==0):
			return root;
		if(string[0]=="1"):
			if(root.right==null):
				return root;
			else:
				find(root.right, string[1:]);
		
		elif(string[0]=="0"):
			if(root.left==null):
				return root;
			else:
				find(root.left, string[1:]);



print("ok");
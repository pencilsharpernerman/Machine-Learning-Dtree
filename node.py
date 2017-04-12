class Node:
	def __init__(self):
		self.label = None
		self.children = {}

	# you may want to add additional fields here...

	def set_label(self, label):
		self.label = label

	def set_children(self, children):
		self.children = children


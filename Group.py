class Group:

	def __init__(self, dictionary, array):
		self.groups = array
		self.groups.append(self) #List of all groups
		self.lookup = dictionary #Reverse node to group lookup
		
		self.all = []
		self.live = []
	
	def add(self, node):
		if node not in self.all:
			self.lookup[node] = self
			self.all.append(node)
	
	def add_live(self, node):
		self.add(node)
		if node not in self.live:
			self.live.append(node)
	
	def get_all_live(self):
		return self.live
	
	def get_all(self):
		return self.all
	
	
	
		
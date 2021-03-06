from Group import Group

class Group_Manager:
	def __init__(self):
		self.group_lookup = {}
		self.all_groups = []
		
	def make_group(self, seed_node):
		g = Group(self.group_lookup, self.all_groups)
		g.add_live(seed_node)
	
	def combine_groups(self, g1, g2):
		if g1 == g2:
			return
		
		#Add nodes to new group
		ng = Group(self.group_lookup, self.all_groups)
		for node in g1.get_all_live() + g2.get_all_live():
			ng.add_live(node)
		for node in g1.get_all() + g2.get_all():
			ng.add(node)
		
		#Remove old groups from the array
		self.all_groups.pop( self.all_groups.index(g1) )
		self.all_groups.pop( self.all_groups.index(g2) )
		#New group was automatically added upon its creation
		
		return ng
	
	def node_in_group(self, node):
		return node in self.group_lookup
		
	def get_group_by(self, node):
		if not self.node_in_group(node):
			raise KeyError("Node does not map to a group.")
		return self.group_lookup[node]
	
	def total_groups(self):
		return len(self.all_groups)
	
	def get_group(self, index):
		return self.all_groups[index]
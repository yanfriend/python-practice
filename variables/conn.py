class Connection:
	verbose=0
	def __init__(self, host):
		self.host=host
	def debug(self, v):
		self.verbose=v
	def connect(self):
		if self.verbose:
			print "connecting to", self.host

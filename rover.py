"""
	For easier Debuging a hash table based approch is done .. :) 
"""
left = {
	'N': 'W',
	'W': 'S',
	'S': 'E',
	'E': 'N'
}

right = {
	'N': 'E',
	'E': 'S',
	'S': 'W',
	'W': 'N'
}

move = {
	'N': (0, 1),
	'E': (1, 0),
	'S': (0, -1),
	'W': (-1, 0)	
}


class Rover:

	def __init__(self, name, (x, y), facing_diection):
		self.name = name
		self.x, self.y = int(x), int(y)
		self.facing_diection = facing_diection


	def left(self):
		self.facing_diection = left[self.facing_diection]

	def right(self):
		self.facing_diection = right[self.facing_diection]

	def move(self):
		self.x = self.x + move[self.facing_diection][0]
		self.y = self.y + move[self.facing_diection][1]

	def echo(self):
		return "%s:%d %d %s"%(self.name, self.x, self.y, self.facing_diection)

if __name__ == "__main__":
	print 'rover'
import unittest
from rover import Rover




class TestRover(unittest.TestCase):

	def test_rover_init(self):
		r = Rover('Rover20', (0, 0), 'W')
		self.assertEqual(r.x, 0, "init: x value wrong")
		self.assertEqual(r.y, 0, "init: y value wrong")
		self.assertEqual(r.name, 'Rover20', "init: name value wrong")
		self.assertEqual(r.facing_diection, 'W', "init: facing_diection value wrong")

	def test_rover_left(self):
		r = Rover('Roverx', (0, 0), 'N')
		r.left()
		self.assertEqual(r.facing_diection, 'W' ,"left to N -> W")
		r.left()
		self.assertEqual(r.facing_diection, 'S' ,"left to W -> S")
		r.left()
		self.assertEqual(r.facing_diection, 'E' ,"left to S -> E")
		r.left()
		self.assertEqual(r.facing_diection, 'N' ,"left to E -> N")
	
	def test_rover_right(self):
		r = Rover('Roverx', (0, 0), 'N')
		r.right()
		self.assertEqual(r.facing_diection, 'E' ,"right to N -> E")
		r.right()
		self.assertEqual(r.facing_diection, 'S' ,"right to E -> S")
		r.right()
		self.assertEqual(r.facing_diection, 'W' ,"right to S -> W")
		r.right()
		self.assertEqual(r.facing_diection, 'N' ,"right to W -> N")
		
	def test_movement(self):
		(x, y) = (0, 0)
		r = Rover('RoverL', (x, y), 'N')
		r.move()
		self.assertEqual((r.x, r.y), (0, 1) ,"1 Move to N")
		r.move()
		self.assertEqual((r.x, r.y), (0, 2) ,"2 Move to N")

		r.right()
		r.move()
		self.assertEqual((r.x, r.y), (1, 2) ,"1 Move to E")
		r.move()
		self.assertEqual((r.x, r.y), (2, 2) ,"2 Move to E")

		r.right()
		r.move()
		self.assertEqual((r.x, r.y), (2, 1) ,"1 Move to S")

		r.left()
		r.move()
		r.move()
		
		self.assertEqual((r.x, r.y), (4, 1) ,"2 Move to E")

	def test_print_format(self):
		r = Rover('Rover101', (5, 5), 'S')
		self.assertEqual(r.echo(), "Rover101:5 5 S" ,"Text format Wrong")



if __name__ == '__main__':
	unittest.main()
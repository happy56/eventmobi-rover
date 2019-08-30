#!/usr/bin/python2.7
from rover import Rover


def main():
	rovers = {}
	#get Plateau:X X
	raw_input()

	while True:
		try:
			a = raw_input()		
			id_ins_type , commands = a.split(':')
			rover_id, ins_type = id_ins_type.split(' ')

			# print '\n\n\nraw : \t\t', a, '\n'
			# print 'id_ins_type : \t\t', id_ins_type 
			# print 'command : \t\t', commands
			# print 'rover id : \t\t', rover_id
			# print 'ins_type : \t\t', ins_type

			if ins_type == 'Landing':
				
				x, y, facing_diection = commands.split(' ')
				rovers[rover_id] = Rover(rover_id, (x, y), facing_diection)
				
				# r = rovers[rover_id]
				# print (r.x, r.y), r.facing_diection

			elif ins_type == 'Instructions':
				for i in commands:
					if i == 'L':
						rovers[rover_id].left()
					elif i == 'R':
						rovers[rover_id].right()
					elif i == 'M':
						rovers[rover_id].move()

		except EOFError as e: 
			break

	for i in rovers.keys()[::-1]:
		print rovers[i].echo()




if __name__ == "__main__":
	main()
from enum import Enum

class Snake:

	def __init__(self):
		self.body = []
		self.body.append(Node(True, Direction.RIGHT, None))

	def add(self):
		snakeLength = len(self.body)
		next = self.body[-1]
		self.body.append(Node(False, next.getDirection(), next))

	def move(self):
		count = 1
		for sp in self.body:
			print(f"Body piece {count}")
			if(sp.isHead()):
				sp.changeDir(Direction.UP)
			sp.move()
			count += 1

		self.body[-1].updateDir()




class Node:

	def __init__(self, head, dir, next):
		self.head = head
		self.direction = dir
		self.next = next
		pass

	def isHead(self):
		return self.head

	def getDirection(self):
		return self.direction

	def getNext(self):
		return self.next

	def move(self):
		# move the SnakePiece in its direction
		if(self.direction == Direction.UP):
			print("UP")
			pass
		elif(self.direction == Direction.RIGHT):
			print("RIGHT")
			pass
		elif(self.direction == Direction.DOWN):
			print("DOWN")
			pass
		elif(self.direction == Direction.LEFT):
			print("LEFT")
			pass

	def updateDir(self):
		if(not self.isHead()):
			self.direction = self.next.direction
			self.next.updateDir()

	def changeDir(self, dir):
		self.direction = dir


class Direction(Enum):
	UP    = 1
	RIGHT = 2
	DOWN  = 3
	LEFT  = 4

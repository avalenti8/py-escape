from random import randint

class Entity:
	def __init__(self, x, y, graphic):
		self.x = x
		self.y = y
		self.graphic = graphic

	def Player(Entity):
		def __init__(self, name, x, y, graphic):
			Entity.__init__(self, x, y, graphic)
			self.hp = hp
			self.cur_hp = cur_hp

		def Move(self, x, y):
			D = input("")
			if D == "n":
				return Player.Move(x, y+1)
			elif D == "s":
				return Player.Move(x, y-1)
			elif D == "w":
				return Player.Move(x-1, y)
			elif D == "e":
				return Player.Move(x+1, y)
	
	def Object(Entity):
		def __init__(self, name, x, y, graphic):
			Entity.__init__(self, x, y, graphic)
			
	
		def Position(self, x, y):
			return Monster.Position(x, y)



#------------------------------------------------------------------
import os 

class Game:
	def __init__(self,room):
		self.room = room
class Room:
	def __init__(self,number):
		self.number = number

	def create_world(self,fileName):
		f = open(fileName)
		a = f.readlines()
		f.close()
		stringa = ''.join(a)
		return stringa
		
room1 = Room(1)
room_created = room1.create_world('room1.txt')
print(room_created)
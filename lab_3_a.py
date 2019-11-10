class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound=sound
		self.name=name
		self.age=age
		self.favorite_color=favorite_color
	def eat(self,food):
		print("Yummy!! "+self.name+" is eating "+food)
	def description(self):
		print(self.name+" is "+self.age+" years old and loves the color "+self.favorite_color)
	def make_sound(self,times):
		print((self.sound+" ")*times)

cat=Animal("meow", "KittyCat", "5","blue")
cat.eat("the whole human race")
cat.description()
cat.make_sound(5)

class Person:
	def __init__(self,name,age,city,gender,favorite_color):
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender
		self.favorite_color=favorite_color
	def eat(self,food):
		print(self.name+" is eating "+food+", he's favorite breakfast")
	def dream(self, dream):
		print(self.name+" dreams about "+dream)
shahar=Person("Shahar","15","Sun House","male","blue")
shahar.eat("Too Many Meems")
shahar.dream("life")


#extra
class Song:
	def __init__(self,lyrics):
		self.lyrics=lyrics
	def sing_me_a_song(self):
		for i in self.lyrics:
			print(i)
song1=Song(["whoo, whoo I'm", "Radioactive, Radioactive"])
song1.sing_me_a_song()


#4
class Bird:
	def __init__(self,name,color,speed):
		self.name=name
		self.color=color
		self.speed=speed

	def GetSpeed(self):
		print(self.name+"'s speed is "+self.speed)
	def Race(self,bird):
		if self.speed>bird.speed:
			print(self.name+" would win the race")
		elif self.speed<bird.speed:
			print(bird.name+" would win the race")
		else:
			print("No one will win the race")
	def sound(self,sound,times):
		print(sound*times)


#Bonus
class Car:
	def __init__(self,color,fuel,speed,fuel_consumption):
		self.color=color
		self.fuel=fuel
		self.speed=speed
		self.fuel_consumption=fuel_consumption
	def piant_car(self,color):
		self.color=color
	def travel(self,time):
		kilometers=self.speed/time
		print("The car traveled "+kilometers+" kilometers")
		self.fuel=fuel-(kilometers*fuel_consumption)
		print("The car has "+self.fuel+" liters of fuel now")
	def race_car(self,car):
		if self.speed>car.speed:
			print("You'r car won")
		elif self.speed<car.speed:
			print("The second car won")
		else:
			print("It's a tie")
	def fill_tank(self,fuel_amount):
		self.fuel+=fuel_amount
My_car=Car("red",)


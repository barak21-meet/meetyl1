class Parrot:
	def __init__(self,name,age,color):
		self.name=name
		self.age=age
		self.color=color
	def fly(self):
		print(self.name+" is flying!")
	def get_color(self):
		print(self.name+" is "+self.color)
	def get_age(self):
		print(self.name+" is "+self.age+" years old")


parrot=Parrot("NO_NAME","2","Green")
parrot.name="YES_NAME"

parrot.get_age()
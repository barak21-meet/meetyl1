class User():
	def __init__(self, name, email, password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.posts=[]
	def add_friend(self, email):
		self.friends_list.append(email)
		print(self.name + " has added "+email+" as a friend")
	def remove_friend(self, email):
		self.friends_list.remove(email)
		print(self.name + " has removed "+email+" from his friend list")
	def post(self, text):
		self.posts.append(text)
		print(self.name+" has posted: "+text)
	def get_userInfo(self):
		print("Name: "+self.name)
		print("Email: "+self.email)
		print("Password: "+self.password)
		print("Friends: "+str(self.friends_list))
		print("Posts: "+str(self.posts))

Ron=User("Ron","ronron@gmail.com","password123")
Shahar=User("Shahar","memebro@gmail.com","the_best_password_ever_made")
Ron.add_friend("memebro@gmail.com")
Ron.post("Hey everyone, I'm Ron and I'm using this app")
Ron.get_userInfo()
Ron.remove_friend("memebro@gmail.com")
Ron.get_userInfo()

nevermind=input("Hello there, press any button to continue ")
while True:
	print("Are you either Ron or Shahar?")
	answer=input("Please answer with either yes or no ")
	
	if answer=="YES" or answer=="yes":
		print("Hi "+self.name)
		quit()
	else:
		print("Ok then, let's make a new user profile")
		name=input("What is your name? ")
		email=input("What is your email? ")
		password=inpot("What password do you want to have? ")
		name=User(name, email, password)

	

f=open("NewFile.txt","w+")
f.write("Text")
f.close()

f=open("NewFile.txt","a+")
f.write("\nNew Text")
f.close()

f=open("NewFile.txt","r")
if f.mode=='r':
	contant=f.read()

print(contant)

fi=f.readlines()
for i in fi:
	print(i)

f.close()
print("HI")

class User:
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.posts=[]
	def add_friend(self,email):
		self.friends_list.append(email)
		print(self.name+" has added "+email+" as a friend")
	def remove_friend(self,email):
		self.friends_list.remove(email)
		print(self.name+" has removed "+email+" from his friend list")
	def post(self,text):
		self.posts.append(text)
		print(self.name+" has posted: "+text)
	def get_userInfo(self):
		print("Name: "+self.name)
		print("Email: "+self.email)
		print("Password: "+self.password)
		print("Friends: "+str(self.friends_list))
		print("Posts: "+str(self.posts))

Shahar=User("Shahar","bro@gmail.com","password")
Ron=User("Ron","ron@gmail.com","123")
Shahar.add_friend("ron@gmail.com")
Shahar.post("This is my first post")
Shahar.get_userInfo()
Shahar.remove_friend("ron@gmail.com")
print("")
print("")
Shahar.get_userInfo()
print("")
print("")
print("")
print("")
print("")
a=1

users1=open("users1.txt","w+")
users1.write("This is the first line\n")
users1.write("\n")
users1.write("User:\n")
users1.write("Name= Shahar\n")
users1.write("Password= password\n")
users1.write("Mail= bro@gmail.com\n")
users1.write("\n")
users1.write("User:\n")
users1.write("Name= Ron\n")
users1.write("Password= 123\n")
users1.write("Email= ron@gmail.com\n")
users1.write("\n")
users1.write("Random line for fun")
users1.write("\n")
users1.close()
post_list=[]
while a>0:
	answer=input("Do you have a user or do you want to sign up? answer with either log to log into your account or sign to sign up\n")
	if answer=="sign":
		print("What is your name?")
		name=input()
		print("What is your email?")
		email=input()
		print("What is going to be your password? *make sure to remember this password")
		password=input()
		users1=open("users1.txt","r")
		text1=users1.read()
		users=open("users.txt","r")
		text=users.read()
		if (name in text) or (name in text1):
			print("")
			print("This name is occupied")
			print("Please try to change the name a little")
			print("Unless you already have a user, in that case, choose log (to log in) and log in to your account")
			print("")
		elif (email in text) or (email in text):
			print("")
			print("This mail is occupied, Are you sure you don't have a user?")
			print("If you're not sure, you can ask Barak Natan Kuchinsky to check if you already have a user")
			print("If you are sure that you don't have a user and the mail is right, someone has probably wrote this email as his")
			print("If that's the case, talk to Barak Kuchinsky and he will find a sulution for you")
			print("If you have a user, then choose log (to log in), otherwise find Barak and ask him about your problem")
			print("")
		elif (password in text) or (password in text1):
			print("")
			print("This password is occupied, please change the password a little...")
			print("Or if you already have a user, choose log (to log in)")
			print("If you have a problem, find Barak Kuchinsky and tell him about it, trust him")
			print("")
		else:
			users=open("users.txt","a")
			users.write("User:\n")
			users.write("Name= "+name+"\n")
			users.write("Password= "+password+"\n")
			users.write("Email= "+email+"\n")
			users.write("\n")
			users.close()
			print("Hello "+name)
			while True:
				print("")
				print("What would you like to do now?")
				print("Your options for now are:  (a) Upload a new post,  (b) add a friend to your friend list,  (c) remove a friend,  (d) see all posts,  (e) quit")
				print("To uplaod a post press 1 and then enter, To add a friend press 2 and then enter, To remvoe a friend press 3 and then enter, To see all posts press 4 and then enter,  To quit just press enter")
				answer=input()
				if answer=='1' or answer=='a':
					print("Write your post")
					post=input()
					post_list.append(name+" has posted: "+post)
					print("You have successfully posted your post")
					print("")
					posts=open("posts.txt","a")
					posts.write("\n")
					posts.write(str(post_list))
					posts.write("\n")
					posts.close()
					move_on=input("Press Enter to continue")
				elif answer=='2' or answer=='b':
					print("What is your new firend's name?")
					friend_name=input()
					print("What is your friend's email?")
					friend_email=input()
					if ((friend_name+" is a friend of "+name) in text) and ((friend_name+" is not a friend of "+name) not in text):
						print(friend_name+" is already a friend of yours")
						print("")
						move_on=input("Press Enter to continue")
					elif (friend_name in text and friend_name in text) or (friend_name in text1 and friend_email in text1):
						print("You have successfully added "+friend_name+" to your friends")
						print("")
						users=open("users.txt","a")
						users.write("\n")
						users.write(friend_name+" is a friend of "+name)
						users.write("\n")
						users.close()
						move_on=input("Press Enter to continue")
					else:
						print("I couldn't seem to find this user in this app, please check that this friend has an account and make sure to check what email he used")
						print("")
						move_on=input("Press Enter to continue")
				elif answer=='3' or answer=='c':
					print("Which friend do you want to remove?")
					friend_name=input()
					print("What is your friend's email?")
					friend_email=input()
					if ((friend_name+" is not a friend of "+name) in text):
						print("This friend has alreasy been removed by you...")
						print("")
						move_on=input("Press Enter to continue")
					elif ((friend_name+" is a friend of "+name) in text):
						print("You have successfully removed "+friend_name+" from your friends")
						print("")
						users=open("users.txt","a")
						users.write("\n")
						users.write(friend_name+" is not a friend of "+name)
						users.write("\n")
						users.close()
						move_on=input("Press Enter to continue")
					else:
						print(friend_name+" is not in your friend list, or the name / the mail you put is wrong...")
						print("")
						move_on=input("Press Enter to continue")
				elif answer=='4' or answer=='d':
					posts=open("posts.txt","r")
					all_posts=posts.readlines()
					print("")
					print(all_posts)
					print("")
					move_on=input("Press Enter to continue")
				else:
					print("Thank you for using this program")
					quit()
			
		#a-=1
	elif answer=="log":
		print("What is your username?")
		name=input()
		print("What is your password?")
		password=input()
		users1=open("users1.txt","r")
		text1=users1.read()
		users=open("users.txt","r")
		text=users.read()
		if (("Name= "+name+"\n"+"Password= "+password) in text) or (("Name= "+name+"\n"+"Password= "+password) in text1):
			print("Hello "+name)
			while True:
				print("")
				print("What would you like to do now?")
				print("Your options for now are:  (a) Upload a new post,  (b) add a friend to your friend list,  (c) remove a friend,  (d) see all posts,  (e) quit")
				print("To uplaod a post press 1 and then enter, To add a friend press 2 and then enter, To remvoe a friend press 3 and then enter, To see all posts press 4 and then enter,  To quit just press enter")
				answer=input()
				if answer=='1' or answer=='a':
					print("Write your post")
					post=input()
					post_list.append(name+" has posted: "+post)
					print("You have successfully posted your post")
					print("")
					posts=open("posts.txt","a")
					posts.write("\n")
					posts.write(str(post_list))
					posts.write("\n")
					posts.close()
					move_on=input("Press Enter to continue")
				elif answer=='2' or answer=='b':
					print("What is your new firend's name?")
					friend_name=input()
					print("What is your friend's email?")
					friend_email=input()
					if ((friend_name+" is a friend of "+name) in text) and ((friend_name+" is not a friend of "+name) not in text):
						print(friend_name+" is already a friend of yours")
						print("")
						move_on=input("Press Enter to continue")
					elif (friend_name in text and friend_name in text) or (friend_name in text1 and friend_email in text1):
						print("You have successfully added "+friend_name+" to your friends")
						print("")
						users=open("users.txt","a")
						users.write("\n")
						users.write(friend_name+" is a friend of "+name)
						users.write("\n")
						users.close()
						move_on=input("Press Enter to continue")
					else:
						print("I couldn't seem to find this user in this app, please check that this friend has an account and make sure to check what email he used")
						print("")
						move_on=input("Press Enter to continue")
				elif answer=='3' or answer=='c':
					print("Which friend do you want to remove?")
					friend_name=input()
					print("What is your friend's email?")
					friend_email=input()
					if ((friend_name+" is not a friend of "+name) in text):
						print("This friend has alreasy been removed by you...")
						print("")
						move_on=input("Press Enter to continue")
					elif ((friend_name+" is a friend of "+name) in text):
						print("You have successfully removed "+friend_name+" from your friends")
						print("")
						users=open("users.txt","a")
						users.write("\n")
						users.write(friend_name+" is not a friend of "+name)
						users.write("\n")
						users.close()
						move_on=input("Press Enter to continue")
					else:
						print(friend_name+" is not in your friend list, or the name / the mail you put is wrong...")
						print("")
						move_on=input("Press Enter to continue")
				elif answer=='4' or answer=='d':
					posts=open("posts.txt","r")
					all_posts=posts.readlines()
					print("")
					print(all_posts)
					print("")
					move_on=input("Press Enter to continue")
				else:
					print("Thank you for using this program")
					quit()
		else:
			print("Not found")
			print("")
			print("Are you sure you entered your name and password correctly?")
			print("Anyway, try again please")
			print("")
		#a-=1

	else:
		print("I didn't understand this answer, I only take log or sign as an answer. please answer again")
		print("")
#I
#just
#Wanted
#to
#make
#it
#300
#lines
#of
#code
#so,
#Here it is!!!
print("working")
import turtle
from turtle import Turtle
class Ball(Turtle):
	def __init__(self,r,color,dx,dy):
		Turtle.__init__(self)
		self.penup()
		self.shape="circle"
		self.size=r/10
		self.r=r
		self.color=color
		self.dx=dx
		self.dy=dy
	def move(self,screen_width,screen_height):
		current_x=self.xcor()
		new_x=current_x+self.dx
		current_y=self.ycor()
		new_y=current_y+self.dy
		right_side_ball=new_x+self.r
		left_side_ball=new_x-self.r
		up_side_ball=new_y+self.r
		down_side_ball=new_y+self.r
		while True:
			if right_side_ball>=screen_width:
				self.goto()


screen_width=turtle.getcanvas().winfo_width()/2
screen_heigh=turtle.getcanvas().winfo_height()/2


print("working so far")
while True:
	ball=Ball(20,"blue",160,160)
	ball.move(150,150)


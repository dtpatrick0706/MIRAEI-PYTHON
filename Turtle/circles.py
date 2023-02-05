from turtle import *

def make_circles():
	bgcolor("blue")
	color("pink")
	speed(0)
	hideturtle()
	
	for i in range(100):
			circle(i*2)
			right(5)
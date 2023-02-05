from turtle import *

def make_pattern():
	color_list = ["purple", "red", "blue", "orange","green"]
	bgcolor("black")

	for i in range(200):
		color(color_list[i%5])
		pensize(i/10+1)
		forward(i)
		left(52)
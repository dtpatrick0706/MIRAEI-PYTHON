import random

blocks=['A', 'B', 'C', 'D']
bridge_piece=[]

def pieces(blocks):
	for i in range(0, 1000):
		piece=[]
		for j in range(random.randint(5,12)):
			piece.append(random.choice(blocks))
		bridge_piece.append(piece)
	return bridge_piece
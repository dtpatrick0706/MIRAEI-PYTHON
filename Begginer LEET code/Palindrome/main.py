# abba, level
# abcba, radar
# racecar, kayak

import creator

total_pieces = creator.pieces(creator.blocks)

# for i in total_pieces:
# 	print(i)
	
print('############################')

for e in total_pieces:
	if len(e)%2 == 0:
		front= e[:len(e)//2]
		back=e[len(e)//2:]
		# print('Front ',end='')
		# print(front)
		# print('Back ', end='')
		# print(back)
		# print('')
		back.reverse()

		if front == back:
			print('******** Palindrome! ********')
			print(e)
	else:
		listlen = len(e)
		front=e[:listlen//2+1]
		back =e[listlen//2:]
		back.reverse()
		
		if front == back:
			print('******** Palindrome! ********')
			print(e)
		
		# reverse = e[::-1]
		# if e == reverse:
		# 	print('******** Palindrome! ********')
		# 	print(e)
		
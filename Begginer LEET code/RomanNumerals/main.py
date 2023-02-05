number = input("What is the roman numeral?")
number = number.upper()
total = 0
previous = ''

for i in number:
	if i == 'I':
		total += 1
		previous = i
	# elif i == 'V'and previous == 'I':
	# 	total += 3
	# 	previous = i
	elif i == 'V':
		total += 5
		if previous == 'I':
			total -= 2
	elif i == 'V' and previous != 'I':
		total += 5
		previous = i
	elif i == 'X' and previous == 'I':
		total += 8
		previous = i
	elif i == 'X' and previous != 'I':
		total += 10
		previous = i
	elif i == 'L':
		total += 50
		previous = i
	elif i == 'C':
		total += 100
		previous = i
	elif i == 'D':
		total += 500
		previous = i
	elif i == 'M':
		total += 1000
		previous = i
	else:
		print('Oops not a Roman numeral')
print(total)
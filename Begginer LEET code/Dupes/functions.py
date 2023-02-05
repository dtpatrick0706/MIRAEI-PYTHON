import random

def list_gen(num_list):
	for i in range(0,10):
		num_list.append(random.randint(1,8))
	return num_list

def dupe_del(num_list, no_dupes):
	for i in num_list:
		if i not in no_dupes:
			no_dupes.append(i)
	return no_dupes


def sorting(no_dupes, sorted):
	not_sorted = True
	while not_sorted:
		smallest = max(no_dupes)
		for i in no_dupes:
			if i < smallest:
				if i not in sorted:
					smallest = i
		sorted.append(smallest)
		if len(no_dupes) == len(sorted):
			not_sorted = False
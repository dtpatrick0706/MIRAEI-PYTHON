from datetime import datetime

class Contact:
	def __init__(self, first_name, middle_name, last_name, date_of_birth, height, weight, phone_number, wears_glasses):
		self.first_name = first_name
		self.middle_name = middle_name
		self.last_name = last_name
		self.date_of_birth = date_of_birth
		self.height = height
		self.weight = weight
		self.phone_number = phone_number
		self.wears_glasses = wears_glasses

	def convert_values_to_strings(self):
		date_of_birth = datetime.strftime(self.date_of_birth, '%Y/%m/%d') #YYYY/MM/DD
		height = str(self.height)
		weight = str(self.weight)
		phone_number = str(self.phone_number)
		wears_glasses = str(self.wears_glasses)
		return [self.first_name, self.middle_name, self.last_name, date_of_birth, height, weight, phone_number, wears_glasses]
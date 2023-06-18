from contact import Contact
from datetime import datetime

contacts = [
	Contact("Devin","Tyler", "Patrick",datetime(1990,7,6), 176, 68, "01064256652", True),
	Contact("Jiyun","","Baek",datetime(2010,4,24), 156.2, 35, "01093423017", False)
]

def convert_contacts_to_table_data():
	contacts_data = []
	for contact in contacts:
		strings = contact.convert_values_to_strings()
		contacts_data.append(strings)
	return contacts_data


def try_to_create_contact(first_name, middle_name, last_name, date_of_birth, height, weight, phone_number, wears_glasses):
	if len(first_name) < 2 or len(last_name) < 2 or date_of_birth == "" or height == "" or weight == "":
		return False
		
	try:
		date_of_birth = datetime.strptime(date_of_birth, '%Y/%m/%d')
		if date_of_birth > datetime.now():
			return False
			
		height = int(height)
		weight = float(weight)
		if height <= 0 or weight <= 0:
			return False
			
		wears_glasses = True if wears_glasses == "True" else False
		contact = Contact(first_name, middle_name, last_name, date_of_birth, height, weight, phone_number, wears_glasses)
		contacts.append(contact)
		return True
	except:
		return False
import PySimpleGUI as sg
import dataFunctions

def read_input_values(values):
	first_name = values["FIRST_NAME"]
	middle_name = values["MIDDLE_NAME"]
	last_name = values["LAST_NAME"]
	date_of_birth = values["DATE_OF_BIRTH"]
	height = values["HEIGHT"]
	weight = values["WEIGHT"]
	phone_number = values["PHONE_NUMBER"]
	wears_glasses = values["WEARS_GLASSES"]
	could_create_contact = dataFunctions.try_to_create_contact(first_name, middle_name, last_name, date_of_birth, height, weight, phone_number, wears_glasses)
	print(first_name, middle_name, last_name, date_of_birth, height, weight, phone_number, wears_glasses)
	return could_create_contact
	
def create_layout():
	return [
		[sg.Text("First name"), sg.Input(key="FIRST_NAME")],
		[sg.Text("Middle name"), sg.Input(key="MIDDLE_NAME")],
		[sg.Text("Last name"), sg.Input(key="LAST_NAME")],
		[sg.Text("Date of birth"), sg.Input(key="DATE_OF_BIRTH"), sg.CalendarButton("Select date", format='%Y/%m/%d')],
		[sg.Text("Height"), sg.Input(key="HEIGHT")],
		[sg.Text("Weight"), sg.Input(key="WEIGHT")],
		[sg.Text("Phone number"), sg.Input(key="PHONE_NUMBER")],
		[sg.Text("Wears glasses"), sg.Checkbox("Yes",key="WEARS_GLASSES")],
		[sg.Cancel(), sg.Button("Save")]
]

def display_new_contact():
	new_contact_layout = create_layout()
	new_contact_window = sg.Window("New Contact", new_contact_layout)

	was_save_successful = False
	
	while True:
		event, values = new_contact_window.read()
		if event == sg.WIN_CLOSED or event == "Cancel":
			break
		elif event == "Save":
			was_save_successful = read_input_values(values)
			if was_save_successful:
				print("Contact Saved")
				break
			else:
				print("Could not save contact")
	new_contact_window.close()
	return was_save_successful
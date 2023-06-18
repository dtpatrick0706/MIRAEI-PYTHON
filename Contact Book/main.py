from dataFunctions import convert_contacts_to_table_data
import PySimpleGUI as sg
import newContactForm

sg.theme("DarkAmber")
## Contacts column titles
table_headings = ["First Name", "Middle Name", "Last Name", "Date of Birth", "Height", "Weight", "Phone Number", "Glasses"]

table_data = convert_contacts_to_table_data()

def press_add_contact_button(contacts_window):
	was_save_successful = newContactForm.display_new_contact()
	if was_save_successful:
		table_data = convert_contacts_to_table_data()
		contacts_window["CONTACTS_TABLE"].update(values= table_data)

## Contacts Window
contacts_window_layout = [
	[sg.Text("All Contacts"), sg.Button("Add new contact")],
	[sg.Table(headings= table_headings, values= table_data, key= "CONTACTS_TABLE")]
]

contacts_window = sg.Window("Contacts List", contacts_window_layout)

## Display contact window
while True:
	event, values = contacts_window.read()
	if event == sg.WIN_CLOSED:
		break
	if event == "Add new contact":
		press_add_contact_button(contacts_window)
contacts_window.close()
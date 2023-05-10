
#############################start of the game###################################
print("\tMan's Homocide\n")
name = input(f'State your name:\n')

print('''Note: You are a detective investigating 
a crime that was commited 1 hour ago at the Henderson 
house hold. You have 7 supects.
''')
input('\t\t\t\t\tEnter to continue')

print('''Note: The victim's name was Josh Henderson. 
32 years old, a lawyer, he was found dead on the first floor in his study. 
The latest suspects: Millie Parker (maid), Georgia Valintine (maid), 
Amina Bradford (maid), Daisie Robies (cook), Elliot Yang (cook), 
Kelsey Henderson (wife) and Alfred Conley (butler)
''')
input('\t\t\t\t\t\tEnter to continue')

##################################################################################
choice = None  
while choice != "0":
	print \
	("""
	       Man's Homocide
	0 - Quit
	1 - Save
	2 - Load
	3 - Suspects statements
	4 - Map
	5 - Inventory
	""")

	choice = input("Option:\n")

#exit:
	if choice == "0":
		print("Good-bye.")

#save:*

###########################################
#loading:*

###########################################

#Suspects statement
	if choice == "3":
		input('''Millie Parker has been a maid in the in the Henderson
house hold for 8 years. She took care of Josh henderson after his parents 
died in a car crash 2 years before he enharited the Henderson house.

Her statement reads: she was in the libary putting some book away that 
Mrs. Henderson gave her and after that she cleaned the libary. Then when to 
the kitchen talking to Elliot about the food he has preparded for Mr. Henderson
''')
		input('\t\t\t\t\t\tEnter to continue')

		print('''---------------------------------------------------------------------
''')
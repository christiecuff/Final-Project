
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
		
		
		
		
		
		
#Shang's Code:

from time import sleep
from random import randint
inventory = []
position = [0, 1]
Weapons = ['knife','pen']
Rooms = ['study','hallway','dining','kitchen','ballroom','library','bathroom','closet','living']
RoomOrder = [['kitchen','hallway','dining'],['library','ballroom','study'],['bathroom','living','closet']]
People = ['maid', 'cook', 'wife', 'butler']
Items = ['book','bucket','mop','music','keys']

#SOLUTION
weapon = None
room = None
murderer = None

def slowPrint(text, delay=0.005):
	for i in text:
		print(i, end='', flush=True)
		sleep(delay)
	print('')

def addItem(item, count):
	if item.lower() in Items and len(inventory)+count <= 15:
		for i in range(count):
			inventory.append(item.lower())
		slowPrint("Item(s) added to inventory")
	elif not item.lower() in Items:
		slowPrint('Item not found, here are the items available:')
		for item in Items:
			slowPrint(item.capitalize())
	elif len(inventory) > 15:
		slowPrint('Inventory is full')

def removeItem(item, count):
	if item in inventory:
		for i in range(count):
			inventory.remove(item)
		slowPrint("Item(s) removed from inventory")
	else:
		slowPrint("Item not in inventory")

def printInventory():
	items = {}
	if len(inventory) > 0:
		slowPrint("Here is your inventory:")
		for item in inventory:
			if item in items:
				items[item] = items[item] + 1
			else:
				items[item] = 1
		for item in items:
			slowPrint(item.capitalize() + ": " + str(items[item]))
	else:
		slowPrint("Your inventory is empty")
		
def move(dir):
	if dir == 'right' and position[1] < 2:
		position[1] += 1
	if dir == 'left' and position[1] > 0:
		position[1] -= 1
	if dir == 'up' and position[0] < 2:
		position[0] += 1
	if dir == 'down' and position[0] > 0:
		position[0] -= 1
		
def printRoom(pos=position):
	print(RoomOrder[pos[0]][pos[1]].capitalize())

def getRandSolution():
	weapon = Weapons[randint(0, len(Weapons))]
	room = Rooms[randint(0, len(Rooms))]
	murderer = People[randint(0, len(People))]
	return (murderer, room, weapon)

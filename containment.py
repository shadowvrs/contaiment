from tkinter import *
from tkinter import simpledialog
import webbrowser
import os
import time
import random
import GameObject

PORTRAIT_LAYOUT = True

ENTRANCE = 1
STORAGE_ROOM = 2
PATHWAY_ONE = 3
OFFICE = 4
PATHWAY_THREE = 5
PATHWAY_TWO = 6
SERVER_ROOM = 7
PATHWAY_FOUR = 8
BREAKER_ROOM = 9
PATHWAY_FIVE = 10
PATHWAY_SIX = 11
CONFERENCE_ROOM = 12
TUNNEL = 13
VOID_ONE = 14
VOID_TWO = 15
VOID_THREE = 16
VOID_FOUR = 17

BACKGROUND_COLOR = "#141a28"
TEXT_BOX_BACKGROUND_COLOR = "#1f2238"
BUTTON_FRAME_BACKGROUND_COLOR = "#1f2238"
BUTTON_BACKGROUND_COLOR = "#2e2c33"

BORDER_COLOR_INACTIVE = "black"
BORDER_COLOR_ACTIVE = "#c8c8c8"

TEXT_COLOR = "white"

BUTTON_FONT = "sans serif"
BUTTON_FONT_SIZE = 12

DOWNLOAD_INFO = """
Download Complete!
25 out of 25 files downloaded

Displaying file objective.tnxt

---Goal---
Your task is to retrive data logs stored on the server in this facility, if you succeed you will be rewarded handsomely.

---Safety---
To avoid any containment breaches, you will be sealed in upon entering. The entrance will be unsealed once you have successfully grabbed the logs.

---Help---
If you ever feel like you don't quite understand something, think of "help" and your neural implant will feed you answers.\n
"""

HELP_INFO = """
\nDisplaying file help.tnxt

---Movement---
Type in the first letter of the direction you wish to go in, so f for forward, l for left, etc. You may also use wasd to move, if you wish.

---Picking up objects---
To pick up any objects, use get or grab.

---Placing objects---
To put down objects or put an object into something, use put or place.

---Getting info on objects or Places---
To get more description on an object, use look or describe command.

---Looking for objects---
You can find objects on people or things using the examine command.

---Using objects---
You can use the command use to use an object. ex: turning off and on a flashlight.
"""

ENTITY_INFO = """
Subject #01482

Risk level: 9
Origin: Unkown
Height: Dynamic

Tests on subject #01482 have shown that it is by far one of the most dangerous subjects contained in this facility.
During tests, subject demonstrated the abilites to exist in multiple locations, disrupt electronics and cause madness to organisms after prolonged exposure.
The absence of light seems to have a calming affect on the subject, whilst light seems to aggravate it to an extreme.
This subject also appears to be constantly distant from the reasurch being done on them, almost like they're day dreaming.
More research and test are required on this subject.
"""

TIP_NOTE_INFO = "Lock the doors and turn off the power immediately it won't be able to see any of us in the dark, wait for me at the exit."

command_widget = None
image_label = None
description_widget = None
inventory_widget = None
forward_button = None
backwards_button = None
right_button = None
left_button = None
flashlight_button = None
root = None

refresh_location = True
refresh_objects_visible = True
power = False
light = False
first_time_entity_activates = True
first_time_using_breaker = True
dead = False
tunnel_created = False
desktop_been_used = False
final_areas = False

current_location = ENTRANCE
turns_entity_is_inactivate = 5
flashlight_power = 10
new_tab = 2
turns_in_room_with_entity = 0

if os.name == "posix":
	url_jumpscare = "pages/index.html"
	path_to_file = os.path.expanduser("~/Desktop")
elif os.name == "nt":
	url_jumpscare = ".\pages\index.html"
	path_to_file = "C:\\Users\\" + os.getlogin() + "\\Desktop"
else:
	url_jumpscare = "pages/index.html"
	path_to_file = os.path.expanduser(" ")

file_name = "security_codes.txt"

flashlight = GameObject.GameObject("Flashlight", 0, True, True, True, False, "A small flashlight with little battery that emits a faint light.")
usb = GameObject.GameObject("USB", 0, True, True, True, False, "A small 32 gigabyte USB, given to you by <<REDACTED>>. It has just enough space for the logs.")

tablet = GameObject.GameObject("Tablet", 0, True, True, False, False, "A small stone tablet with strange symbols carved around a hole directly in the middle of the tablet.")
acid_jar = GameObject.GameObject("Container of Acid", 0, True, True, False, False, "A small metal container containing acid.")

debris_one = GameObject.GameObject("Debris", PATHWAY_FIVE, False, True, False, False, "Debris from the celling fills the passage ahead, if you look closely through the gaps in the rocks and boulders, you're able to see an opening into another room, you might be able to get there if you could only find a way to remove the rocks.")
debris_two = GameObject.GameObject("Debris", PATHWAY_SIX, False, True, False, False, "Debris from the celling fills the passage ahead.")

breaker = GameObject.GameObject("Breaker", BREAKER_ROOM, False, True, False, False, "An old rusty breaker, it could be used to turn on the power.")
shelve = GameObject.GameObject("Shelve", STORAGE_ROOM, False, True, False, False, "An old shelve containing several aged tools, items and products.")
desktop_office = GameObject.GameObject("Desktop", OFFICE, False, True, False, False, "An old triple monitor computer, it requires a password and a username to get into it.")
desktop_server_room = GameObject.GameObject("Desktop", SERVER_ROOM, False, True, False, False, "An old computer hooked up to a server containing all files on this facility.")
securit_keypad = GameObject.GameObject("Keypad", PATHWAY_TWO, False, True, False, False, "A small keypad requiring a four digit code.")

door_pathway_one = GameObject.GameObject("Door", PATHWAY_ONE, False, True, False, False, "A metal plated door, there is no way you're going to break it.")
door_pathway_two = GameObject.GameObject("Door", PATHWAY_TWO, False, True, False, False, "A metal plated door, there is no way you're going to break it.")

corpse_one = GameObject.GameObject("Corpse", PATHWAY_TWO, False, True, False, False, "A dead body with claw marks covering them.")
corpse_two = GameObject.GameObject("Corpse", PATHWAY_THREE, False, True, False, False, "A dead body with claw marks covering them.")
corpse_three = GameObject.GameObject("Corpse", PATHWAY_FIVE, False, True, False, False, "A dead body with claw marks covering them.")
corpse_four = GameObject.GameObject("Corpse", CONFERENCE_ROOM, False, True, False, False, "A dead body with claw marks covering them.")

tip_note = GameObject.GameObject("Sticky Note", 0, True, True, False, False, "A small piece of paper with nothing on it, unless viewed through the tablet.")
note_login_info = GameObject.GameObject("Password Note", 0, True, True, False, False, "A small piece of paper with a passcode written on it.")

notes_entity = GameObject.GameObject("Entity Notes", 0, True, False, False, False, "Lab notes on a subject of this facility.")

battery_one = GameObject.GameObject("Battery", 0, True, True, False, False, "A small battery with barely any charge left.")
battery_two = GameObject.GameObject("Battery", 0, True, True, False, False, "A small battery with barely any charge left.")
battery_three = GameObject.GameObject("Battery", 0, True, True, False, False, "A small battery with barely any charge left.")
battery_four = GameObject.GameObject("Battery", 0, True, True, False, False, "A small battery with barely any charge left.")
battery_five = GameObject.GameObject("Battery", ENTRANCE, True, True, False, False, "A small battery with barely any charge left.")
battery_six = GameObject.GameObject("Battery", OFFICE, True, True, False, False, "A small battery with barely any charge left.")

entity_one = GameObject.GameObject("???", 0, False, True, False, False, "???")
entity_two = GameObject.GameObject("???", 0, False, True, False, False, "???")

game_objects = [usb, flashlight, shelve, breaker, desktop_office, desktop_server_room, securit_keypad, debris_one, debris_two, 
door_pathway_one, door_pathway_two, corpse_one, corpse_two, corpse_three, corpse_four, tablet, acid_jar, tip_note, note_login_info,
notes_entity, entity_one, entity_two, battery_one, battery_two, battery_three, battery_four, battery_five, battery_six]

def perform_command(verb, noun):
	if verb == "F" or verb == "B" or verb == "R" or verb == "L" or verb == "W" or verb == "S" or verb == "A" or verb == "D":
		perform_go_command(verb)
	elif verb == "FORWARDS" or verb == "FORWARD" or verb == "BACKWARD" or verb == "BACKWARDS" or verb == "BACK" or verb == "RIGHT" or verb == "LEFT":
		perform_go_command(verb)		
	elif verb == "GET" or verb == "GRAB":
		perform_get_command(noun)
	elif verb == "PUT" or verb == "PLACE":
		perform_put_command(noun)
	elif verb == "LOOK" or verb == "DESCRIBE":
		perform_look_command(noun)
	elif verb == "EXAMINE":
		perform_examine_command(noun)
	elif verb == "READ":
		perform_read_command(noun)
	elif verb == "USE":
		perform_use_command(noun)
	elif verb == "HELP":
		perform_help_command()
	else:
		print_to_description("Unknown command.\n")

def perform_go_command(direction):
	global current_location
	global refresh_location
	global light
	
	if light:
		if (direction == "F" or direction == "W" or direction == "FORWARD" or direction == "FORWARDS"):
			new_location = get_location_forward()
		elif (direction == "B" or direction == "S" or direction == "BACKWARD" or direction == "BACKWARDS" or direction == "BACK"):
			new_location = get_location_backward()
		elif (direction == "R" or direction == "D" or direction == "RIGHT"):
			new_location = get_location_right()
		elif (direction == "L" or direction == "A" or direction == "LEFT"):
			new_location = get_location_left()
		else:
			new_location = 0
		
		if (new_location == 0):
			print_to_description("You can't go that way.\n")
		else:
			determine_flashlight_power()

			if dead == False:
				current_location = new_location
				refresh_location = True
				turns_in_room_with_entity = 0
			
			set_current_state()
	else:
		print_to_description("It's too dark to move.\n")
	

def perform_get_command(object_name):
	global light
	global refresh_objects_visible

	game_object = get_game_object(object_name, True)

	if light:
		if not (game_object is None):
			if (game_object.location != current_location or game_object.visible == False):
				print_to_description("Specify an object to pick up.\n")
			elif (game_object.movable == False):
				print_to_description("You can't pick it up!\n")
			else:
				#pick up the object
				game_object.carried = True
				refresh_objects_visible = True
				print_to_description("You picked up " + object_name.lower() + ".\n")
		else:
			print_to_description("Specify an object to pick up.\n")
	else:
		print_to_description("You are unable to pickup any items, it's too dark.\n")

	can_entity_kill()

def perform_put_command(object_name):
	global light
	global final_areas
	global turns_in_room_with_entity
	global refresh_objects_visible

	game_object = get_game_object(object_name, False, True)
	
	if light:
		if not (game_object is None) and (game_object.carried):
			if game_object == flashlight:
				print_to_description("You can't put down that object.\n")
			elif game_object == usb and desktop_server_room.location == current_location:
				print_to_description("You put the usb into the desktop and grab all the files retaining to <<REDACTED>>.\n")
				final_areas = True
			else:
				#put down the object
				game_object.location = current_location
				game_object.carried = False
				game_object.visible = True
				refresh_objects_visible = True
				print_to_description("You put down " + object_name.lower() + ".\n")
		else:
			print_to_description("You are not carrying one of those.\n")
	else:
		print_to_description("It's too dark to put down any items.\n")

	can_entity_kill()

def perform_look_command(object_name):
	global sword_found
	global refresh_location
	global refresh_objects_visible
	global light
	
	game_object = get_game_object(object_name)
 
	if not (game_object is None):
		if light:
			if (game_object.carried) or (game_object.visible):
				print_to_description(game_object.description)
			else:
				#recognized but not visible
				print_to_description("You can't see one of those.\n")
		else:
			print_to_description("It's too dark to see any objects.\n")

	else:
		if (object_name == ""):
			if light:
				#generic LOOK
				refresh_location = True
				refresh_objects_visible = True
			else: 
				print_to_description("It's too dark to discern the location you're in.\n")
		else:
			#not visible recognized
			print_to_description("You can't see one of those.\n")

	can_entity_kill()

def perform_read_command(object_name):
	game_object = get_game_object(object_name)

	if not (game_object is None):
		if (game_object == notes_entity):
			if (notes_entity.carried):
				print_to_description("You read the note:\n" + ENTITY_INFO)
			elif (notes_entity.visible):
				print_to_description("You can't read it from a distance.\n")
			else:
				print_to_description("Object does not exist.\n")
		elif (game_object == note_login_info) and (note_login_info.carried):
				print_to_description("You read the card:\nUsername: Connar\nPassword: 0451\n")
		elif (game_object == tip_note) and (tip_note.carried):
			print_to_description("You read the sticky note:\n" + TIP_NOTE_INFO)
		else:
			if ((game_object.visible == False) and (game_object.carried == False)):
				print_to_description("Object does not exist.\n")
			else:
				print_to_description("There is nothing to read that object.\n")
	else:
		print_to_description("Object does not exist.\n")

	can_entity_kill()

def perform_examine_command(object_name):
	game_object = get_game_object(object_name)

	if not (game_object is None) and game_object.visible:
		if game_object.examined == False:
			if game_object == shelve:
				print_to_description("You search the shelve hoping to find a weapon, but instead you find a metal container of industrial acid and a battery.\n")
				acid_jar.carried = True
				battery_three.carried = True
			elif game_object == debris_two:
				print_to_description("You examine the pile and find a battery under one of the rocks.\n")
				battery_two.carried = True
			elif game_object == corpse_one:
				print_to_description("You examine the corpse and find a small stone tablet with strange symbols carved around a hole directly in the middle of it and a small sticky note with nothing written on it. You look through the hole in the middle of the tablet, and are suddenly able to see words on the sticky note. You put the tablet and the note into your inventory.\n")
				tablet.carried = True
				tip_note.carried = True
			elif game_object == corpse_three:
				print_to_description("You examine the corpse and find a battery.\n")
				battery_one.carried = True
			elif game_object == corpse_four:
				print_to_description("You examine the corpse and find a small piece of paper with a username and password written on it.\n")
				note_login_info.carried = True
			else:
				print_to_description("You don't find anything.\n")
			
			game_object.examined = True
		else:
			print_to_description("You've already searched this thing.\n")
	else:
		print_to_description("Specify a object to examine.\n")


def perform_use_command(object_name):
	global power
	global flashlight_power
	global light
	global tunnel_created
	global first_time_using_breaker
	global desktop_been_used
	global flashlight_power

	user_response = None

	game_object = get_game_object(object_name)

	if not (game_object is None) and game_object.visible:
		if game_object == flashlight and game_object.carried:
			if light:
				light = False
				print_to_description("You turn off the light.\n")
				can_entity_kill()
			else:
				light = True
				print_to_description("You turn on the light.\n")

			set_current_image()
		elif game_object == tablet and game_object.carried:
			if light:
				if desktop_been_used and desktop_office.location == current_location:
					print_to_description("You look through the tablet and are able to see text appear in the file.\n")
					try:
						with open(os.path.join(path_to_file, file_name), 'a') as game:
							game.write("\nServer room code: 2367")
					except:
						with open(os.path.join(path_to_file, file_name), 'a') as game:
							game.write("\nServer room code: 2367")
				elif notes_entity.visible == False and notes_entity.location == current_location:
					notes_entity.visible = True
					print_to_description("You look through the tablet and see lab notes scattered on the ground.\n")
				else:
					print_to_description("You look through the tablet, but you don't see anything new in the room.\n")					
			else:
				print_to_description("It's too dark to see through the tablet.\n")
		elif (game_object == battery_one) or (game_object == battery_two) or (game_object == battery_three) or (game_object == battery_four) or (game_object == battery_five) or (game_object == battery_six):
			flashlight_power += 6

			if flashlight_power > 10:
				flashlight_power = 10
				print_to_description("You replace the old battery with a new one, your flashlight's battery is now at 100%.\n")
			else:
				print_to_description("You replace the old battery with a new one.\n")
				determine_flashlight_power()

			game_object.carried = False
			game_object.location = 0

		elif game_object == breaker:
			if light:
				if first_time_using_breaker:
					print_to_description("ERROR: unknown access to neural implant.\nYou flip the switches on the breaker, all power is restored.\n")
					try:
						webbrowser.open(url_jumpscare, new=new_tab)
					except:
						print_to_description("\nI SEE YOU\n")

					power = True		
					door_pathway_one.visible = False
					first_time_using_breaker = False					
				else:
					print_to_description("Breaker has already been used.\n")
			else:
				print_to_description("It's too dark to use the breaker.\n")
		elif game_object == desktop_office:
			if light:
				if desktop_been_used == False:
					if note_login_info.carried:
						use_desktop()
					else:
						user_response = simpledialog.askstring("Containment", "Enter Passcode", parent=root)

						if user_response == "0451":
							use_desktop()
						else:
							print_to_description("The computer denies the passcode.")
				else:
					print_to_description("You are already login into the computer.\n")
			else:
				print_to_description("It's too dark to use the computer.\n")
		elif game_object == desktop_server_room:
			print_to_description("You open up the computer and try to look through the files on the computer but-\nUNAUTHORISED THOUGHT, please put the usb into the computer.\n")
		elif game_object == acid_jar:
			if light:
				user_response = simpledialog.askstring("Containment", "On what?", parent=root)
				new_game_object = get_game_object(user_response)

				if not (new_game_object is None):
					if new_game_object == debris_one:
						print_to_description("Little by little, you pour the acid onto the rocks and boulders until you're able to make a very unstable tunnel that you can barely fit in.\n")
						tunnel_created = True
						acid_jar.carried = False
						acid_jar.location = 0
					elif user_response == door_pathway_two.name.lower():
						print_to_description("You pour a little bit of acid onto the door, but it is unable to dissolve the metal of the door.\n")
					elif user_response == corpse_one.name.lower() or user_response == corpse_two.name.lower() or user_response == corpse_three.name.lower() or user_response == corpse_four.name.lower():
						print_to_description("You think about pouring the acid on the corpse, but then you realise that you're not a horrible person.\n")
					elif user_response == entity_one.name.lower() or user_response == entity_two.name.lower():
						print_to_description("Quickly you grab your jar of acid and splash ??? with it.\nThe acid passes through the entity and onto the floor.\n")
					else:
						print_to_description("You can't use the jar of acid on that.\n")
				else:
					print_to_description("Object doesn't exist.\n")
			else:
				print_to_description("It's probably not a good idea to use a jar of acid in the dark.\n")
		elif game_object == securit_keypad:
			if light:
				if power:
					user_response = simpledialog.askstring("Containment", "Enter passcode", parent=root)
					if user_response == "2367":
						print_to_description("You put the password into the keypad. The door immediately opens.\n")
						door_pathway_two.visible = False
					else:
						print_to_description("The keypad flashes red, you put in the wrong code.\n")
				else:
					print_to_description("You try to use the keypad, but it doesn't have any power.\n")
			else:
				print_to_description("You can't use the keypad in the dark.")
		else:
			print_to_description("You can't use that object.\n")

		if game_object != flashlight:
			can_entity_kill()
	else:
		print("this ran")
		print_to_description("Specify which object to use.\n")

def perform_help_command():
	print_to_description(HELP_INFO)

def describe_current_location():
	current_room = ""

	if (current_location == ENTRANCE):
		current_room = "Entrance"
	elif (current_location == STORAGE_ROOM):
		current_room = "Storage Room"
	elif (current_location == PATHWAY_ONE) or (current_location == PATHWAY_THREE) or (current_location == PATHWAY_TWO) or (current_location == PATHWAY_FOUR) or (current_location == PATHWAY_FIVE) or (current_location == PATHWAY_SIX):
		current_room = "Pathway"
	elif (current_location == OFFICE):
		current_room = "Office"
	elif (current_location == SERVER_ROOM):
		current_room = "Server Room"
	elif (current_location == CONFERENCE_ROOM):
		current_room = "Conference Room"
	elif (current_location == TUNNEL):
		current_room = "Tunnel"
		print_to_description("You're barely able to move, but you slowly manage to crawl through the narrow tunnel of your creation.")
	elif (current_location == BREAKER_ROOM):
		current_room = "Breaker Room"
	elif (current_location == VOID_ONE) or (current_location == VOID_TWO) or (current_location == VOID_THREE) or (current_location == VOID_FOUR):
		flashlight_button.config(state = "disabled")
		current_room = "???"
		if (current_location) == VOID_THREE:
			print_to_description("I have been trapped in here for so long, memories and pain given to me only for the enjoyment of others.\nI am done now... no more pain, no more containment.")
		if (current_location == VOID_FOUR):
			delete_everything()
	else:
		current_room = "Unknown location:" + current_location

	print_to_description("Location: " + current_room)
	
def set_current_image():
	if dead == False:
		if light:
			if entity_one.location == current_location or entity_two.location == current_location:
				if (current_location == ENTRANCE):
					image_label.img = PhotoImage(file = "res/entity/entrance.gif")
				elif (current_location == STORAGE_ROOM):
					image_label.img = PhotoImage(file = "res/entity/storage_room.gif")
				elif (current_location == PATHWAY_ONE):
					if power == False:
						image_label.img = PhotoImage(file = "res/entity/pathway_one.gif")
					else:
						image_label.img = PhotoImage(file = "res/entity/pathway_one_door_open.gif")
				elif (current_location == OFFICE):
					image_label.img = PhotoImage(file = "res/entity/control_room.gif")
				elif (current_location == SERVER_ROOM):
					image_label.img = PhotoImage(file = "res/entity/server_room.gif")
				elif (current_location == PATHWAY_TWO):
					if door_pathway_two.visible or not (power):
						image_label.img = PhotoImage(file = "res/entity/pathway_two.gif")
					else:
						image_label.img = PhotoImage(file = "res/entity/pathway_two_door_open.gif")
				elif (current_location == PATHWAY_THREE):
					image_label.img = PhotoImage(file = "res/entity/pathway_three.gif")
				elif (current_location == PATHWAY_FOUR):
					image_label.img = PhotoImage(file = "res/entity/pathway_four.gif")
				elif (current_location == PATHWAY_FIVE):
					image_label.img = PhotoImage(file = "res/entity/pathway_five.gif")
				elif (current_location == PATHWAY_SIX):
					image_label.img = PhotoImage(file = "res/entity/pathway_six.gif")
				elif (current_location == BREAKER_ROOM):
					image_label.img = PhotoImage(file = "res/entity/breaker_room.gif")
				elif (current_location == CONFERENCE_ROOM):
					image_label.img = PhotoImage(file = "res/entity/conference_room.gif")
				else:
					image_label.img = PhotoImage(file = "res/blank-1.gif")
			else:
				if (current_location == ENTRANCE):
					image_label.img = PhotoImage(file = "res/normal/entrance.gif")
				elif (current_location == STORAGE_ROOM):
					image_label.img = PhotoImage(file = "res/normal/storage_room.gif")
				elif (current_location == PATHWAY_ONE):
					if power == False:
						image_label.img = PhotoImage(file = "res/normal/pathway_one.gif")
					else:
						image_label.img = PhotoImage(file = "res/normal/pathway_one_door_open.gif")
				elif (current_location == OFFICE):
					image_label.img = PhotoImage(file = "res/normal/control_room.gif")
				elif (current_location == SERVER_ROOM):
					image_label.img = PhotoImage(file = "res/normal/server_room.gif")
				elif (current_location == PATHWAY_TWO):
					if door_pathway_two.visible or not (power):
						image_label.img = PhotoImage(file = "res/normal/pathway_two.gif")
					else:
						image_label.img = PhotoImage(file = "res/normal/pathway_two_door_open.gif")
				elif (current_location == PATHWAY_THREE):
					image_label.img = PhotoImage(file = "res/normal/pathway_three.gif")
				elif (current_location == PATHWAY_FOUR):
					image_label.img = PhotoImage(file = "res/normal/pathway_four.gif")
				elif (current_location == PATHWAY_FIVE):
					if tunnel_created:
						image_label.img = PhotoImage(file = "res/normal/pathway_five_hole.gif")
					else:
						image_label.img = PhotoImage(file = "res/normal/pathway_five.gif")
				elif (current_location == PATHWAY_SIX):
					image_label.img = PhotoImage(file = "res/normal/pathway_six.gif")
				elif (current_location == BREAKER_ROOM):
					image_label.img = PhotoImage(file = "res/normal/breaker_room.gif")
				elif (current_location == TUNNEL):
					image_label.img = PhotoImage(file = "res/normal/tunnel.gif")
				elif (current_location == CONFERENCE_ROOM):
					image_label.img = PhotoImage(file = "res/normal/conference_room.gif")
				elif (current_location == VOID_ONE):
					image_label.img = PhotoImage(file = "res/void_one.gif")
				elif (current_location == VOID_TWO):
					image_label.img = PhotoImage(file = "res/void_two.gif")
				elif (current_location == VOID_THREE) or (current_location == VOID_FOUR):
					image_label.img = PhotoImage(file = "res/void_three.gif")
				else:
					image_label.img = PhotoImage(file = "res/blank-1.gif")
		else:
			image_label.img = PhotoImage(file = "res/normal/darkness.gif")
	else:
		image_label.img = PhotoImage(file = "res/game_over.gif")
		
	image_label.config(image = image_label.img)
		
def get_location_forward():
	if final_areas == False:
		if (current_location == ENTRANCE):
			return PATHWAY_ONE
		elif (current_location == PATHWAY_ONE):
			return PATHWAY_TWO
		elif (current_location == PATHWAY_TWO):
			return PATHWAY_FIVE
		elif (current_location == PATHWAY_FOUR):
			return BREAKER_ROOM
		elif (current_location == PATHWAY_FIVE) and (tunnel_created):
			return TUNNEL
		elif (current_location == TUNNEL):
			return PATHWAY_SIX
		else:
			return 0
	else:
		if current_location == VOID_ONE:
			return VOID_TWO
		elif current_location == VOID_TWO:
			return VOID_THREE
		elif current_location == VOID_THREE:
			return VOID_FOUR
		else:
			return 0

def get_location_backward():
	if (current_location == PATHWAY_ONE):
		return ENTRANCE
	elif (current_location == STORAGE_ROOM):
		return PATHWAY_THREE
	elif (current_location == PATHWAY_THREE):
		return PATHWAY_TWO
	elif (current_location == PATHWAY_TWO):
		return PATHWAY_ONE
	elif (current_location == PATHWAY_FOUR):
		return PATHWAY_THREE
	elif (current_location == PATHWAY_FIVE):
		return PATHWAY_TWO
	elif (current_location == CONFERENCE_ROOM):
		return PATHWAY_SIX
	elif (current_location == BREAKER_ROOM):
		return PATHWAY_FOUR
	elif (current_location == PATHWAY_SIX):
		return TUNNEL
	elif (current_location == TUNNEL):
		return PATHWAY_FIVE
	elif (current_location == SERVER_ROOM):
		return PATHWAY_TWO if not final_areas else VOID_ONE
	elif (current_location == OFFICE):
		return PATHWAY_ONE
	else:
		return 0

def get_location_right():
	if (current_location == PATHWAY_TWO):
		return PATHWAY_THREE
	elif (current_location == PATHWAY_THREE):
		return STORAGE_ROOM
	else:
		return 0

def get_location_left():
	if (current_location == PATHWAY_ONE) and (power):
		return OFFICE 
	elif (current_location == PATHWAY_THREE):
		return PATHWAY_FOUR
	elif (current_location == PATHWAY_TWO) and (door_pathway_two.visible == False) and (power):
		return SERVER_ROOM
	elif (current_location == PATHWAY_SIX):
		return CONFERENCE_ROOM
	else:
		return 0
		
def get_game_object(object_name, only_check_object_location=False, only_check_object_carried=False):
	sought_object = None
	for current_object in game_objects:
		if (current_object.name.upper() == object_name.upper()):
			sought_object = current_object
			if only_check_object_location == True:
				if (current_location == sought_object.location):
					break
				else:
					sought_object = None
			elif only_check_object_carried == True:
				if sought_object.carried:
					break
				else:
					sought_object = None
			else:
				if (current_location == sought_object.location) or sought_object.carried:
					break
				else:
					sought_object = None

	return sought_object

def describe_current_visible_objects():
	object_count = 0
	object_list = ""

	for current_object in game_objects:
		if ((current_object.location == current_location) and (current_object.visible) and (current_object.carried == False)):
			object_list = object_list + (", " if object_count > 0 else "") + current_object.name
			object_count = object_count + 1
	if object_count > 0:
		print_to_description("You see: " + object_list + "\n") 
	else:
		print_to_description("\n")

def describe_current_inventory():
	object_count = 0
	object_list = ""

	for current_object in game_objects:
		if (current_object.carried):
			object_list = object_list + (", " if object_count > 0 else "") + current_object.name
			object_count = object_count + 1
	
	inventory = "---Inventory---\nYou are carrying:\n" + (object_list if object_count > 0 else "Nothing")
	
	inventory_widget.config(state = "normal")
	inventory_widget.delete(1.0, END)
	inventory_widget.insert(1.0, inventory)
	inventory_widget.config(state = "disabled")

def print_to_description(output, user_input=False):
	description_widget.config(state = 'normal')
	description_widget.insert(END, output + "\n")
	description_widget.config(state = 'disabled')
	description_widget.see(END)

def use_desktop():
	print_to_description("You put in the login info from the dead body into the computer. You login and immediately start scowering for anything useful, eventually you find an odd file on computers desktop named 'security_codes.txt'.\n")
	try:
		with open(os.path.join(path_to_file, file_name), 'w') as game:
			game.write("Use the all seeing eye.")
	except:
		with open(os.path.join("", file_name), 'w') as game:
			game.write("Use the all seeing eye.")
	desktop_been_used = True

def determine_flashlight_power():
	global flashlight_power
	global light
	global turns_in_room_with_entity

	current_power = "100%"

	if not current_location >= VOID_ONE:
		flashlight_power -= 1

		if flashlight_power == 9:
			current_power = "90%"
		elif flashlight_power == 8:
			current_power = "80%"
		elif flashlight_power == 7:
			current_power = "70%"
		elif flashlight_power == 6:
			current_power = "60%"
		elif flashlight_power == 5:
			current_power = "50%"
		elif flashlight_power == 4:
			current_power = "40%"
		elif flashlight_power == 3:
			current_power = "30%"
		elif flashlight_power == 2:
			current_power = "20%"
		elif flashlight_power == 1:
			current_power = "10%"
		else:
			current_power = "0%"
			light = False
			flashlight_button.config(state = "disabled")

		can_entity_kill()

		if not dead:
			print_to_description("Your flashlight has: " + current_power + " power remaining.")

def assign_random_room():
	room = random.randrange(ENTRANCE, TUNNEL)
	return room

def can_entity_kill():
	global dead
	global flashlight_power
	global first_time_entity_activates
	global turns_in_room_with_entity
	global turns_entity_is_inactivate

	if current_location == entity_one.location or current_location == entity_two.location or flashlight_power <= 0:
		if (light and turns_in_room_with_entity >= 1) or flashlight_power <= 0:
			if not flashlight_power <= 0:
				print_to_description("With one quick slash, you fall to the ground, dead.")
			else:
				print_to_description("Your flashlight turns off, you try to turn it back on, but it refuses.\nYou start moving around the room, trying to find your way around, until you hear a terible sound, followed by immense pain in your body, you collapse to the ground. As your vision fades, you see one red eye staring at you.")
			dead = True
			set_current_state()
		else:
			entity_one.location = 0
			entity_two.location = 0
			turns_entity_is_inactivate += 3
	else:
		if turns_entity_is_inactivate <= 0:
			if first_time_entity_activates:
				print_to_description("You hear a loud scream echoing from the halls.\n")
				first_time_entity_activates = False

			entity_one.location = assign_random_room()

			if power:
				entity_two.location = assign_random_room()

				while entity_one.location == entity_two.location:
					entity_two.location = assign_random_room()
		else:
			turns_entity_is_inactivate -= 1

		turns_in_room_with_entity += 1
	
	set_current_image()

def delete_everything():
	with open(os.path.join("", "credits.txt"), 'w') as game:
		game.write("Created by: Cole K")
	if os.name == "posix":
		os.system("rm containment.py && rm GameObject.py && rm -r pages && rm -r res && rm -r __pycache__")
	elif os.name == "nt":
		os.system("del containment.py & del GameObject.py & rmdir /Q /S pages & rmdir /Q /S res && rmdir /Q /S __pycache__")
	else:
		print("Error")
	quit()

def build_interface():
	global flashlight_button
	global command_widget
	global image_label
	global description_widget
	global inventory_widget
	global forward_button
	global backwards_button
	global right_button
	global left_button	
	global root

	root = Tk()
	root.resizable(0,0)
	root.config(bg = BACKGROUND_COLOR)
	root.title("Containment")
	
	image_label = Label(root)
	if (PORTRAIT_LAYOUT):
		image_label.grid(row=0, column=0, columnspan=3, padx = 2, pady = 2)
	else:
		image_label.grid(row=0, column=0, rowspan=3, columnspan=1,padx = 2, pady = 2)

	description_widget = Text(root, bg = TEXT_BOX_BACKGROUND_COLOR, fg = TEXT_COLOR, highlightbackground=BORDER_COLOR_INACTIVE, highlightcolor=BORDER_COLOR_ACTIVE, width=60, height=25, relief=GROOVE, wrap='word')
	description_widget.insert(1.0, DOWNLOAD_INFO)
	description_widget.config(state = "disabled")
	if (PORTRAIT_LAYOUT):
		description_widget.grid(row=1, column=0, columnspan=3, sticky=W, padx=2, pady =2)
	else:
		description_widget.grid(row=0, column=1, rowspan=1, columnspan=2, padx=2, pady =2)

	command_widget = Entry(root, bg=TEXT_BOX_BACKGROUND_COLOR, fg=TEXT_COLOR, highlightbackground=BORDER_COLOR_INACTIVE, highlightcolor=BORDER_COLOR_ACTIVE, width=(25 if PORTRAIT_LAYOUT else 54))
	command_widget.bind('<Return>', return_key_enter)
	if (PORTRAIT_LAYOUT):
		command_widget.grid(row=2, column=0, padx = 2, pady = 2)
	else:
		command_widget.grid(row=1, column=1, rowspan=1, columnspan=2)
	
	button_frame = Frame(root)
	button_frame.config(bg=BUTTON_FRAME_BACKGROUND_COLOR, highlightbackground=BORDER_COLOR_INACTIVE, highlightcolor=BORDER_COLOR_ACTIVE, height = 150, width = 150, relief = GROOVE)
	if (PORTRAIT_LAYOUT):
		button_frame.grid(row=3, column=0, columnspan =1, padx = 2, pady = 2)
	else:
		button_frame.grid(row=2, column=1, columnspan =1, padx = 2, pady = 2)

	forward_button = Button(button_frame, font=(BUTTON_FONT, BUTTON_FONT_SIZE), bg = BUTTON_BACKGROUND_COLOR, fg = TEXT_COLOR, highlightbackground=BORDER_COLOR_INACTIVE, text = "↑", width = 3)
	forward_button.grid(row=0, column=1, padx = 2, pady = 2)
	forward_button.config(command = forward_button_click)
	
	backwards_button = Button(button_frame, font=(BUTTON_FONT, BUTTON_FONT_SIZE), bg = BUTTON_BACKGROUND_COLOR, fg = TEXT_COLOR, highlightbackground=BORDER_COLOR_INACTIVE, text = "↓", width = 3)
	backwards_button.grid(row=2, column=1, padx = 2, pady = 2)
	backwards_button.config(command = backwards_button_click)

	right_button = Button(button_frame, font=(BUTTON_FONT, BUTTON_FONT_SIZE), bg = BUTTON_BACKGROUND_COLOR, fg = TEXT_COLOR, highlightbackground=BORDER_COLOR_INACTIVE, text = "→", width = 3)
	right_button.grid(row=1, column=2, padx = 2, pady = 2)
	right_button.config(command = right_button_click)

	left_button = Button(button_frame, font=(BUTTON_FONT, BUTTON_FONT_SIZE), bg = BUTTON_BACKGROUND_COLOR, fg = TEXT_COLOR, highlightbackground=BORDER_COLOR_INACTIVE, text = "←", width = 3)
	left_button.grid(row=1, column=0, padx = 2, pady = 2)
	left_button.config(command = left_button_click)

	flashlight_button = Button(button_frame, font=(BUTTON_FONT, BUTTON_FONT_SIZE), bg = BUTTON_BACKGROUND_COLOR, fg = TEXT_COLOR, highlightbackground=BORDER_COLOR_ACTIVE, text = "🗲", width = 3)
	flashlight_button.grid(row=1, column=1)
	flashlight_button.config(command = lambda: perform_use_command("flashlight"))
	
	inventory_widget = Text(root, bg = TEXT_BOX_BACKGROUND_COLOR, fg = TEXT_COLOR, highlightbackground=BORDER_COLOR_INACTIVE, highlightcolor=BORDER_COLOR_ACTIVE, width = (30 if PORTRAIT_LAYOUT else 38), height = (8 if PORTRAIT_LAYOUT else 6), relief = GROOVE , state=DISABLED )
	if (PORTRAIT_LAYOUT):
		inventory_widget.grid(row=2, column=2, rowspan = 2, padx = 2, pady = 2,sticky=W)
	else:
		inventory_widget.grid(row=2, column=2, rowspan = 2, padx = 2, pady = 2,sticky=W)
	
def set_current_state():
	global refresh_location
	global refresh_objects_visible

	if (dead == False):
		if (refresh_location):
			describe_current_location()
			set_current_image()
		
		if (refresh_location or refresh_objects_visible):
			describe_current_visible_objects()

		set_directions_to_move()
		describe_current_inventory()
	else:
		command_widget.config(state = "disabled")
		forward_button.config(state = "disabled")
		backwards_button.config(state = "disabled")
		left_button.config(state = "disabled")
		right_button.config(state = "disabled")
		flashlight_button.config(state = "disabled")

	refresh_location = False
	refresh_objects_visible = False

def forward_button_click():
	perform_command("F", "")

def backwards_button_click():
	perform_command("B", "")

def right_button_click():
	perform_command("R", "")

def left_button_click():
	perform_command("L", "")

def return_key_enter(event):
	if event.widget == command_widget:
		command_string = command_widget.get()
		print_to_description(command_string, True)

		command_widget.delete(0, END)
		words = command_string.split(' ', 1)
		verb = words[0]
		noun = (words[1] if (len(words) > 1) else "")
		perform_command(verb.upper(), noun.upper())
		
		set_current_state()

def set_directions_to_move():

	move_to_north = (get_location_forward() > 0) and (dead == False)
	move_to_south = (get_location_backward() > 0) and (dead == False)
	move_to_east = (get_location_right() > 0) and (dead == False)
	move_to_west = (get_location_left() > 0) and (dead == False)
	
	forward_button.config(state = ("normal" if move_to_north else "disabled"))
	backwards_button.config(state = ("normal" if move_to_south else "disabled"))
	right_button.config(state = ("normal" if move_to_east else "disabled"))
	left_button.config(state = ("normal" if move_to_west else "disabled"))

def main():
	notes_entity.location = assign_random_room()
	battery_four.location = assign_random_room()

	build_interface()
	set_current_state()

	root.mainloop()
		
main()
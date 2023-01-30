# Changelog:
# v1.0: Initial release of the game
# v1.1: Fixed up various bugs and formatting errors. Included a main menu which gives the user the ability to adjust text speed.

import time 
import random
import sys
name = ""
def speak(char):
    for letter in char:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(textspeed)
textspeed = 0.03

inventory = []
red = '\033[91m'
end = '\033[0m'
blue = '\033[94m'
bold = '\033[1m'

def menu(): #User is given the option of starting the game or adjusting the text speed.
    print("""
  _____                                                   __                 _             
 |  __ \                                                 / _|     /\        (_)            
 | |  | |_   _ _ __   __ _  ___  ___  _ __  ___     ___ | |_     /  \    ___ _ _ __   __ _ 
 | |  | | | | | '_ \ / _` |/ _ \/ _ \| '_ \/ __|   / _ \|  _|   / /\ \  / __| | '_ \ / _` |
 | |__| | |_| | | | | (_| |  __/ (_) | | | \__ \  | (_) | |    / ____ \ \__ \ | | | | (_| |
 |_____/ \__,_|_| |_|\__, |\___|\___/|_| |_|___/   \___/|_|   /_/    \_\ ___/_|_| |_|\__,_|
                      __/ |                                                              
 """)
    print("Welcome to Dungeons of Asina. Would you like to start the game or view options?")
    print("1: Start Game")
    print("2. Options")
    answer = input("Enter 1 or 2: ")
    if answer == "1":
        start()
    elif answer == "2":
        options()
    else:
        menu()

def options(): #User can proceed to adjust text speed or return to main menu
    print("-----------------")
    print("Options\n")
    print("1. Text Speed")
    print("2. Back")
    answer = input("Enter 1 or 2: ")
    if answer == "1":
        text_speed()
    elif answer =="2":
        menu()

def text_speed(): # User can set their text speed to slow, medium or fast and then returned to the main menu
    global textspeed
    print("-------------")
    print("Select the speed you would like your text to move at.\n")
    print("1. Slow")
    print("2. Medium")
    print("3. Fast")
    print("4. Main Menu")
    answer = input("Enter 1, 2, 3 or 4: ")
    if answer == "1":
        textspeed = 0.05
        print("You have changed your text speed to:\nSlow\n\nReturning to main menu.")
        time.sleep(2)
        menu()
    elif answer == "2":
        textspeed = 0.03
        print("You have changed your text speed to:\nMedium\nReturning to main menu.")
        time.sleep(2)
        menu()
    elif answer == "3":
        textspeed = 0.01
        print("You have changed your text speed to:\nFast\n\nReturning to main menu.")
        time.sleep(2)
        menu()
    else:
        print("\nYour text speed has not been changed\n\nReturning to main menu")
        time.sleep(2)
        menu()

def start(): #Start of the game. The user is prompted to enter their name.
    global name
    name = input("What is your name?: ")
    print(f"Welcome {name}!")
    print("You are an adventurer in the dungeons of Asina Prison")
    print("You will be given the opportunity to explore multiple locations and collect items as you go.")
    print("Be careful what you do and where you go, as the wrong choice could lead to your demise...")
    print(f"Good luck, {name}")
    time.sleep(3)
    game_start()

def game_start(): #First room, players must get the torch, search the room, pick up the key and use it on the door. (path complete)  
    speak("You awaken in a dark room. In front of you, you see a dimly lit torch on the wall and a gate ahead of you.\nWhat do you do? ")
    speak("\n1. Pick up the torch")
    speak("\n2. Try to open the gate\n")
    answer = input("Enter 1 or 2: ")
    if answer == "2":
        locked_gate_no_torch()
    elif answer == "1":
        torch()
    else:
        answer_fail()

def torch(): #If the player choses to pick up the torch. (complete)
    speak("\nYou pick up the torch.\nWhat do you do now?")
    speak("\n1. Try to open the gate.")
    speak("\n2. Look around the room.\n")
    answer = input("Enter 1 or 2: ")
    if answer == "1":
        locked_gate_torch()
    elif answer == "2":
        look_around_room()
    else:
        answer_fail()

def locked_gate_no_torch(): # No torch, no key. (complete)
    speak("\nThe door is locked and the room is too dark for your to figure out the mechanism.\nWhat do you do?")
    speak("\n1. Pick up the torch")
    speak("\n2. Try to open the gate\n")
    answer = input("Enter 1 or 2: ")
    if answer == "2":
        locked_gate_no_torch()
    elif answer == "1":
        torch()
    else:
        answer_fail()

def look_around_room(): # Search for the key with the torch. If the user opts to wait, they die. (complete)
    speak("\nYou look around the room and find a key glistening in the corner. You pick up the key.\nWhat do you do now?")
    speak("\n1. Use the key on the door.")
    speak("\n2. Wait.\n")
    answer = input("Enter 1 or 2: ")
    if answer == "1":
        locked_gate_key()
    elif answer == "2":
        game_over("While you sit around waiting, suddenly a green gas starts to flood the room. You find yourself struggling to breathe, until finally, everything goes black.\n")
    else:
        answer_fail()
    
def locked_gate_torch(): # Player has the torch, but no key. Must search the room. (complete)
    speak("\nEven with the light of the torch you still can't figure out the gate. It seems like you need a key.\n")
    speak("\nWhat do you do now?")
    speak("\n1. Try the gate again.")
    speak("\n2. Look around the room.\n")
    answer = input("Enter 1 or 2: ")
    if answer == "1":
        locked_gate_torch()
    elif answer == "2":
        look_around_room()
    else:
        answer_fail()
        
def locked_gate_key(): # Player has the key, is presented with the option of going left or right. (complete)
    speak("\nYou use the key on the gate. \nYou step out and see two hallways. One to the left and one to the right \nWhere do you go?")
    speak("\n1. Left")
    speak("\n2. Right\n")
    answer = input("Enter 1 or 2: ")
    if answer == "1":
        first_corridor_left()
    elif answer == "2":
        first_corridor_right()
    else:
        answer_fail()

def first_corridor_left(): # if they player opts to go left. (complete)
    speak("\nYou find yourself in an open, well-lit room.\nIn the middle of the room is a table with a drink on it labelled 'Drink this, you'll need it.'\nBeyond the table is an open door. \nWhat do you do?")
    speak("\n1. Drink the drink")
    speak("\n2. Ignore the drink")
    speak("\n3. Go back and take the right corridor.\n")
    answer = input("Enter 1, 2 or 3: ")
    if answer == "1":
        table_drink()
    elif answer == "2":
        no_drink_door()
    elif answer == "3":
        first_corridor_right()
    else:
        answer_fail()

def table_drink(): # room with drink on table. Player must drink the drink in order to continue. (complete)
    speak("\nYou approach the table and take a sip of the drink. You can't figure out the taste but it is incredible. You down the rest of the drink. \nYou feel a strange sensation in your body, but nothing happens immediately.")
    speak("\nWhat do you do now?")
    speak("\n1. Go through the door.")
    speak("\n2. Turn around and go through the right corridor.\n")
    answer = input("Enter 1 or 2: ")
    if answer == "1":
        drink_door()
    elif answer == "2":
        first_corridor_right()
    else:
        answer_fail()
    
def drink_door(): # Player drinks the drink, they do not succumb to poison and can continue. At this point they are locked in and can not go back until they pick up the map. (complete)
    speak("\nImbued with whatever effect the drink has, you head through the open door. \nAs you step into the room the door slams shut behind you. \nAfter a moment, green gas starts to slowly fill the room. Strangely, it has no effect on you.")
    speak("\nYou look around the room and see a skeleton sat against the wall. On the other side of the room, you see a door.\nWhat do you do?")
    speak("\n1. Approach the skeleton")
    speak("\n2. Try the door.\n")
    answer = input("Enter 1 or 2: ")
    if answer == "1":
        examine_skeleton()
    elif answer == "2":
        try_door()
    else:
        answer_fail()

def no_drink_door(): #Player does not drink the drink. They can return to the right path or die. (complete)
    speak("\nYou decide to ignore the drink. What do you do now?")
    speak("\n1. Continue through the door")
    speak("\n2. Turn around and go through the corridor on the right.\n")
    answer = input("Enter 1 or 2: ")
    if answer == "1":
        game_over("You continue through the door ahead of you. As you step into the room, the door slams shut behind you. \nAfter a moment, green gas starts to slowly fill the room. You feel the gas filling your lungs and find it harder and harder to breath. \nThen, everything goes dark.")
    elif answer == "2":
        first_corridor_right()
    else:
        answer_fail()

def examine_skeleton(): # Player chooses to examine the skeleton. 
    speak("\nYou walk up to the skeleton and begin to examine it. In its lifeless hands, you see a shining silver sword, and a map laying on the floor next to it.\nWhat do you do?")
    speak("\n1. Take the sword.")
    speak("\n2. Take the map")
    speak("\n3. Take the sword and map.")
    speak("\n4. Ignore the skeleton and try to open the door ahead.\n")
    answer = input("Enter 1, 2, 3 or 4: ")
    if answer == "1" or answer == "3":
        game_over("You reach down to pick up the sword. As you begin to pick up the sword, you hear the clacking of bones and the skeleton tightens it's grip on the sword as it comes to life. The skeleton stands and raises the sword. \nSuddenly, the sword comes crashing down, making contact with your skull. \nEverything goes dark.")
    elif answer == "2":
        map_get()
    elif answer == "4":
        try_door()
    else:
        answer_fail()

def try_door(): # Player attempts to open the door, unsuccesful.
    speak("\nThe door seems to be locked with no visible mechanism to open it.\n You seem to have no other option but to examine the skeleton.")
    speak("\n1. Examine the skeleton\n")
    answer = ("Enter 1 to continue: ")
    if answer == "1":
        examine_skeleton()
    else:
        answer_fail()

def map_get(): # Player obtains the map, door unlocks. Examine map, continue or go back. 
    speak("\nYou reach down and pick up the map. As you pick up the map, you hear a small click, and both doors open.\nWhat do you do now?")
    inventory.append("map")
    speak("\n1. Examine the map.")
    speak("\n2. Continue to the next room.")
    speak("\n3. Go back and return to the right-hand corridor.\n")
    answer = input("Enter 1, 2 or 3: ")
    if answer == "1":
        map_get_examine()
    elif answer == "2":
        guard_room()
    elif answer == "3":
        first_corridor_right()
    else:
        answer_fail()

def map_get_examine(): # Player examines the map.
    speak("\nYou unfold the map and take a look. It appears to be incomplete, but should contain some information to help you on your journey.\nIt contains a layout with a handful of rooms in the dungeon. Certain rooms have symbols on them, possibly marking their contents. \n In the room ahead of you, you see a small symbol that looks like a sword of some description. Ahead of that, you see a room marked with a skull.\nIn what looks like the corridor on the right, you see a tick symbol.\nWhat do you do?")
    speak("\n1. Continue on to the room ahead.")
    speak("\n2. Turn around, and go back.\n")
    answer = input("Enter 1 or 2: ")
    if answer == "1":
        guard_room()
    elif answer == "2":
        first_corridor_right()
    else:
        answer_fail()

def guard_room(): # Player enters the guard room
    speak("\nYou approach the door and continue on to the next room. \nIn the room, you see 6 beds, 3 lined up on either side of the wall. Next to each bed is a chest.\nThe room appears to be sleeping quarters for the prison's guards. The room is messy and ramshackled, as if everyone left in a hurry.\nOn the other side of the room is an open door.\nWhat do you do?")
    speak("\n1. Search the chests")
    speak("\n2. Continue on to the next room\n")
    answer = input("Enter 1 or 2: ")
    if answer == "1":
        search_chests()
    elif answer == "2":
        game_over("You continue on to the next room. As you step through the doorway, spikes shoot out of either and impale your body\nEverything goes dark.")
    else:
        answer_fail()

def search_chests(): # Player chooses to search chests.
    speak("\nUpon inspection of the chests, all but one seem to be open and empty. You approach the closed chest and open it. Inside you find the following items:\nA blunt short sword\nA small health potion\nA rope\nDo you take the items?")
    speak("\n1. Yes")
    speak("\n2. No\n")
    answer = input("Enter 1 or 2: ")
    if answer == "1":
        chest_pickup()
    elif answer == "2":
        chest_ignore()

def chest_pickup(): # Player decides to take the items in the chest.
    speak("\nYou pick up the items")
    inventory.extend(["sword", "small health potion","rope"])
    print("\n-------------------")
    print("Your inventory now contains: ")
    for i in inventory:
        print(i)
    speak("\nWhat do you do now?")
    speak("\n1. Continue to the next room")
    speak("\n2. Go back to the right-hand corridor\n")
    answer = input("Enter 1 or 2: ")
    if answer == "1":
        game_over("You continue on to the next room. As you step through the doorway, spikes shoot out of either and impale your body\nEverything goes dark.")
    elif answer == "2":
        first_corridor_right()
    else:
        answer_fail()

def chest_ignore(): # Player decides not to take the items
    speak("\nYou decide to ignore the items in the chest\nWhat do you do now?")
    speak("\n1. Continue to the next room")
    speak("\n2. Return to the right-hand corridor\n")
    answer = input("Enter 1 or 2: ")
    if answer == "1":
        game_over("You continue on to the next room. As you step through the doorway, spikes shoot out of either and impale your body\nEverything goes dark.")
    elif answer == "2":
        first_corridor_right

def first_corridor_right(): #Path for if the user choses to take the right path. Path locks.
    speak("\nFrom the jail cell, you head down the corridor to your right.\nYou step into the room and the door slams closed behind you. There seems to be no way back. In the room, you see a small ledge with a hook on it. It is too tall to climb, but a rope might help you. At the end of the room, you see a door.\nWhat do you do?")
    if "rope" in inventory:
        speak("\n1. Use the rope to climb the ledge")
        speak("\n2. Continue through the door.\n")
        answer = input("Enter 1 or 2: ")
        if answer == "1":
            rope_ledge()
            inventory.remove("rope")
        elif answer == "2":
            skill_check_room()
        else:
            answer_fail()
    elif "rope" not in inventory:
        speak("\n1. Continue through the door.")
        speak("\n2. Attempt to climb the ledge.\n")
        answer = input("Enter 1 or 2: ")
        if answer == "1":
            skill_check_room()
        elif answer == "2":
            ledge_climb()
        else:
            answer_fail()

def rope_ledge(): #If the player has the rope or succeeds the climbing skill check.
    speak("\nAfter reaching the top of the ledge, you see a low tunnel. You crawl through to the low tunnel, which slowly beings to open up.\nAs you reach the end of the tunnel, you see a grand palace hall. Magnificient chandeliers hang from the rooftops and the walls are adorned with gold.\nAs you scan the room, you see dozens of bodies strewn across the floor, with blood splattered everywhere.\nFortunately, it seems like whatever has slain these creatures has gone. For now. But you're sure this isn't the end.\n")
    game_complete()

def skill_check_room(): # Entrance to the skill check room. Players can continue or turn back and try their luck
    speak("\nYou find yourself in yourself on a narrow bridge, evidently filled with danger. You're going to need all your wits about you if you are going to survive this route. If only you could climb that ledge...\nWhat do you do?")
    speak("\n1. Go back and try and climb the ledge")
    speak("\n2. Continue through the room.\n")
    answer = input("Enter 1 or 2: ")
    if answer == "1" and "rope" in inventory:
        rope_ledge()
    elif answer == "1" and "rope" not in inventory:
        ledge_climb()
    elif answer == "2":
        skill_checks()

def skill_checks(): # 3 skill checks with ramping difficulty.
    speak("\nOkay... well it was your choice. Looking ahead, you, the first obstacle you see is an axe swinging from the ceiling. There is no way around it.\nWhat do you do?")
    speak("\n1. Try and dash passed the swinging axe.\n")
    input("Enter 1 to continue: ")

    if random.randint(0,100) >= 50:
        speak("\nYou wait for the axe's swing to reach its peak. You dash through and feel a gush of air blow against your back as the axe crashes down behind you.\nNext, you see a large, heavy boulder in front of you. Behind that is a large gap in the path.\nIt seems as though you could push the boulder into the gap and continue forward, but its going to be harder than dodging the axes.\nWhat do you do?")
        speak("\n1. Push the boulder")
        input("\nEnter 1 to continue: ")
        if random.randint(0,100) >= 60:
            speak("\nYou summon all of your strength and push the boulder forward. The boulder comes loose and starts to roll. You hear a THUD as the boulder falls into the gap, making way for you to cross.\nFinally, the end is in sight, and you can see the door just a few steps ahead of you.\nSuddenly, an overwhelming thought begins to flood your brain")
            speak(red + "\nYou will not continue...\nThis is the end for you..." + end )
            print("\nYour mind is flooded, you have no choice but to fight the voice. This will be your toughest challenge yet.")
            if random.randint(0,100) >= 75:
                speak(blue + bold + "\nQUIET" + end + " you yell, as you focus your mind. The voice in your end gets louder and louder until... nothing")
                print("\nThe voice in your head seems to be gone. For now at least. You continue forward through the door")
            elif random.randint(0,100) < 75:
                game_over(red + "You are done. We are free..." + end + "\nYou fail to fight back the voice.\nEverything goes black\n")
        elif random.randint(0,100) < 60:
            game_over("You gather all of your strength and attempt to push the boulder forward. The boulder comes loose and starts to roll. Unfortunately for you, the boulder rolls backwards and crushes you.\nEverything goes black.")
    elif random.randint(0,100) < 50:
        game_over("You wait for the axe's swing to reach its peak. Unfortunately you are too slow, and as you dash through the axe swings down, chopping your body in half.\nEverything goes black. ")
    
def ledge_climb(): # Player attempts to climb ledge.
    speak("You attempt to climb the ledge.")
    if random.randint(0,100) < 70:
        speak("\nMustering every ounce of strength in your body, defying all odds you manage to climb the ledge.\n")
        rope_ledge()
    else:
        game_over("You attempt to climb the ledge. Using every ounce of strength in your body, you start to climb. Around half way up the ledge, you start to lose your grip. Suddenly, a rock in the wall gives way. You fall to the ground and a rock lands on your head.\nEverything goes black.")

def skill_check_pass(): #If the player succeeds at all skill checks.
    speak("\nYou step out into a grand palace hall. Magnificient chandeliers hang from the rooftops and the walls are adorned with gold.\nAs you scan the room, you see dozens of bodies strewn across the floor, with blood splattered everywhere.\nFortunately, it seems like whatever has slain these creatures has gone. For now. But you're sure this isn't the end.\n")
    game_complete()

def game_over(reason): # If the user dies, they are referred here and told the reason.
    speak("\n" + reason)
    print("You have died. Would you like to try again?")
    print("1. Yes")
    print("2. No")
    answer = input("Enter 1 or 2: ")
    if answer == "1":
        game_start()
    else:
        print("Thanks for playing.")
        quit()

def answer_fail(): # If the user does not input a correct answer they are killed and given the chance to restart here. (complete)
    print("You fail to make a correct choice in time. Without warning, the life drains from your body.\nYou have died. Would you like to try again?")
    print("1. Yes")
    print("2. No")
    answer = input("Enter 1 or 2: ")
    if answer == "1":
        game_start()
    else:
        print("Thanks for playing.")
        quit()

def game_complete(): # If the player completes the game
    print(f"Congratulations, {name}, you have completed 'Dungeons of Asina'! That's all there is for now, but you still need to find out who (or what) attacked the palace.\nThank you for playing!")
    quit()


menu()
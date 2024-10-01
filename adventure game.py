inventory=[]

def start():
    print("You are standing outside your front door calling for your cat. Do you walk further outside or do you go back inside and trust he will show up")
    answer=input("Do you go (n)orth or (s)outh\n>")
    if answer=="n":
        movenorth()
    elif answer == "s":
        movesouth()
    else:
        print("Not a valid input")
        

def movenorth():
    print("You walk further outside and suddenly the ground begins to rumble and you here a distant roar. Will you go l(eft) towards the sound or go r(ight)\n>?")
    monsterChoice = input("l or r\n>")
    if monsterChoice =="l":
        print("The roaring is getting lowder and lowder soon you approach a door. You hear a faint meow. Will you enter?")
        print("You instanlly freeze as you see the horrifying monster before you")
        fightmonster()
        start()
    elif monsterChoice=="r":
        print("Smart choice! You should check it out later. Maybe next time bring something to defend yourself with")
    else:
        ("Not a valid input")
    
def movesouth():
    print("You go back inside, still worried for your cat. All of a sudden the ground begins to rumble and you here a distant roar")
    print("Your granny is calling you from the sitting room. Do you go to her? (Yes or No))
    grannyChoice = input 

def getsword():
    global inventory
    print("You got the sword")
    inventory.append("sword")

def fightmonster():
    global inventory
    if "sword" in inventory:
        print("You killed the monster")
    else:
        print("You had no weapon you were killed")

start()
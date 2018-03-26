"""
    adventureGame.py
    Dylan Grandjean
    September 26th, 2016

    A first look at an adventure game which has the player
    walking through four different environments.
"""

def easternGarden():
    print "\nYou find yourself on the grass, facing what looks like it once \n"\
          "was a great structure, but only rubbles are left of its former \n"\
          "glory. On your left, to the south, the remnants of what was once \n"\
          "a door frame still holds, testamony of the structure's strong \n"\
          "architecture which has survived the passing of time. On your \n"\
          "right, the northern wall seems to have collapsed, and an \n"\
          "oppening can be spotted, leading to the darkness that resides \n"\
          "inside this timeless structure.\n"
    direction = raw_input("Which way do you choose to go?\n(N)orth?\n(S)outh?\n(Q)uit\n--> ").upper()
    while direction != "N" and direction != "S" and direction != "Q":
        direction = raw_input("There only seem to be two ways out of this garden.\nWhich way do you choose to go?\n(N)orth?\n(S)outh?\n(Q)uit\n--> ").upper()
    return direction
    
def westernPlatform(end):
    print "\nA cold wind rushes towards you as you step outside. You feel your eyes \n"\
          "water as a wave of chill takes over your body. You wipe the tears from \n"\
          "your eyes and clasp your hands together in the hope of keeping them warm. \n"\
          "As you look around, you find yourself on a circular platform made of metal\n"\
          "and protruding off a cliff. Strange marks were covering the entire surface \n"\
          "of the platform, like scratches. What sort of claws could have left such \n"\
          "markings in such a strong material? You look over the platform and can \n"\
          "hardly make out the shape of trees below. A uneasy feeling takes over, \n"\
          "and a lump forms in your throat as you step away from the edge. You \n"\
          "look one more time at your surroundings. From where you stand, chains \n"\
          "of mountains can be seen in the horizon, and an endless forest \n"\
          "lies under you. You turn around, facing the building once more. On the \n"\
          "southern side of the structure, a hole leads to what looks like a room. \n"\
          "On the northern side, a sliding door gives access to the inside of the \n"\
          "building, and furniture can be seen through the glass.\n"
    if end == True:
        return endingQuestion()
    else:           
        direction = raw_input("Which way do you choose to go?\n(N)orth?\n(S)outh?\n(Q)uit\n--> ").upper()
        while direction != "N" and direction != "S" and direction != "Q":
            direction = raw_input("There only seem to be two ways out of this bedroom.\nWhich way do you choose to go?\n(N)orth?\n(S)outh?\n(Q)uit\n--> ").upper()
        printed = False
        return direction, printed

def southernWing(end):
    print "\nAfter carefully entering the room, you take a look around and recognize \n"\
          "what seems to have been a bed. The mattress seems to have been eaten \n"\
          "by bugs, and little is left of the sheets. After taking a closer look \n"\
          "at the wall, you realize they seem to be made of steel, and what looked \n"\
          "like rubbles earlier is, in fact, a melted portion of the structure. \n"\
          "What happened here? Towards the west, a hole stands where there was \n"\
          "once a window, and through it, you seem to be able to spot clouds. \n"\
          "On your right, towards the east, the familiar smell of grass and pine \n"\
          "reaches your nostrils.\n"
    if end == True:
        return endingQuestion()
    else:
        direction = raw_input("Which way do you choose to go?\n(E)ast?\n(W)est?\n(Q)uit\n--> ").upper()
        while direction != "E" and direction != "W" and direction != "Q":
            direction = raw_input("There only seem to be two ways out of this bedroom.\nWhich way do you choose to go?\n(E)ast?\n(W)est?\n(Q)uit\n--> ").upper()
        printed = False
        return direction, printed

def northernWing(end):
    print "\nAs you step into the room, you notice that the ground is covered by a \n"\
          "red carpet which kept the atmosphere of the room as warm and welcoming \n"\
          "as it must have been from the first day. Old burned furniture are \n"\
          "scattered around the room, and as you make your way to one of them, \n"\
          "you hear a crack under your shoe. You look down and pick up a picture \n"\
          "frame portaying a family: a man, a woman, and two children. Was this \n"\
          "their house? What could have happened here? A fire was your first \n"\
          "thought, however, only certain sections of the room were burnt, \n"\
          "making it even more peculiar. On your right, towards the west, \n"\
          "a glass sliding door which seems to have survived the fire's \n"\
          "wrath gives way to the outside. On your left, towards the \n"\
          "east, you can see the grass and the trees of the garden \n"\
          "you woke up in earlier.\n"
    if end == True:
        return endingQuestion()
    else:
        direction = raw_input("Which way do you choose to go?\n(E)ast?\n(W)est?\n(Q)uit\n--> ").upper()
        while direction != "E" and direction != "W" and direction != "Q":
            direction = raw_input("There only seem to be two ways out of this bedroom.\nWhich way do you choose to go?\n(E)ast?\n(W)est?\n(Q)uit\n--> ").upper()
        printed = False
        return direction, printed

def checkEnd(west, north, south, printed):
    if west == True and north == True and south == True and printed == False:
            return True
        
def endingQuestion():
    print "\nA loud noise seems to have come from the garden, perhaps you should investigate!"
    direction = raw_input("(I)nvestigate? --> ").upper()
    while direction != "I":
        direction = raw_input("There is no turning back now.. \n(I)nvestigate?\n --> ").upper()
    printed = True
    return direction, printed


def ending():
    print "\nAs you run outside, you find the debris of a helicopter which seems \n"\
          "to have crahed in the garden. A movement catches your eyes, the pilot \n"\
          "is alive. You run towards him as he struggles to free himself from \n"\
          "the vehicle. As you approach, you realize he does not have long to \n"\
          "live. He turn towards you, his eyes filled with fear and whisper in \n"\
          "one last breath.\n"\
          "\"You should not have come here..\"\n"\
          "You feel the temperature quickly rising on your neck, and every inch \n"\
          "of your body compels you to run away. But as you turn around, fire \n"\
          "is all you can see. An instense amount of heat surrounds you, \n"\
          "a scream could be heard. You soon realize you are the one screeming. \n"\
          "And then nothing.."

def main():
    end = False
    west = False
    north = False
    south = False
    printed = False
    done = False

    
    print "\nRays of light are shinning through your eyelids. You are wrapped \n"\
          "in a warm feeling of comfort and peace. Where are you? How did you \n"\
          "get here? A fresh breeze grazes your skin as these questions arise \n"\
          "and you slowly open your eyes, not yet accustomed to the brightness \n"\
          "of your surroudings."

    direction = easternGarden()

    while done == False:
        if direction == "N":
            north = True
            end = checkEnd(west, north, south, printed)
            direction, printed = northernWing(end)
        elif direction == "E":
            direction = easternGarden()
        elif direction == "W":
            west = True
            end = checkEnd(west, north, south, printed)
            direction, printed = westernPlatform(end)
        elif direction == "S":
            south = True
            end = checkEnd(west, north, south, printed)
            direction, printed = southernWing(end)
        elif direction == "I":
            done = True
        elif direction == "Q":
            done = True

    if direction == "I":
        ending()
                
main()
    

#Réda Alidrissi-Omari
#261068776

ROOM_NAME = "That middle room between the entrance and the main hall"
AUTHOR = "Réda"
PUBLIC = True

def victory_message():
    """()->None
    prints a victory message and an ending to the story
    >>> victory_message()
    Wowzers, it worked! As you slowly open the door you find your friend sitting on his couch watching TV.
    When you asked him how he warped inside, he told you casually that he just entered while you took a stupid picture.
    You then ask him why you can't open the door without its key when your inside, and he just tells you that it is a security measure.
    You then proceed to criticize him for putting his second door's key under a rug and about his book taste (even if you don't know what the book was even about) and that's it, you escaped, kind of.
    
    """
    print("Wowzers, it worked! As you slowly open the door you find your friend sitting on his couch watching TV.")
    print("When you asked him how he warped inside, he told you casually that he just entered while you took a stupid picture.")
    print("You then ask him why you can't open the door without its key when your inside, and he just tells you that it is a security measure.")
    print("You then proceed to criticize him for putting his second door's key under a rug and about his reading taste (even if you don't know what the book was even about) and that's it, you escaped, kind of.")
 
def escape_room():
    """()->None
    prints a textual interactive excape room game where the user inputs various commands to interact with
    the objects in frotn of him.
        
    >>> escape_room()
    You were walking with a friend towards his house. In front of it you find a beautiful ladybug and proceed to take a picture of it. 
    When you turn around, you couldn't find your friend.
    You assume he entered while you were busy, so upon opening the main door, you found a narrow room.
    When you enter the room,  the door behind you closes shut and you have no way of leaving. 
    Weird, you think to yourself...

    Next to you, there is a table with a book and a half empty mug on top, below you is an old looking rug,
    and in front of you is another door.
    What will you do next?

    > asdasfaf
    You have entered an invalid command. Type list commands to see all the valid commands to type!

    > list commands
    examine table
    pick up book
    check mug
    examine rug
    open door

    > table
    You approach the table in front of you, it is slightly dusty. You look at the book and the mug.

    > look under rug
    You notice that you are standing on an old and dusty looking rug.
    After remembering how in movies most protagonists are stupid enough to put their keys under their entrance rug, 
    which is a very dumb trope that movies should stop to use. It is ridiculous, how did they get away with it for so long, it is always used as a plot developement device when it is such a stupid and uncommon thing to do. A kid would figure this out. 
    Anyway, after checking under it you find a key, as you expected. Dissapointing.

    > put key in door
    Wowzers, it worked! As you slowly open the door you find your friend sitting on his couch watching TV.
    When you asked him how he warped inside, he told you casually that he just entered while you took a stupid picture.
    You then ask him why you can't open the door without its key when your inside, and he just tells you that it is a security measure.
    You then proceed to criticize him for putting his second door's key under a rug and about his book taste (even if you don't know what the book was even about) and that's it, you escaped, kind of.


    >>> escape_room()
    You were walking with a friend towards his house. In front of it you find a beautiful ladybug and proceed to take a picture of it. 
    When you turn around, you couldn't find your friend.
    You assume he entered while you were busy, so upon opening the main door, you found a narrow room.
    When you enter the room,  the door behind you closes shut and you have no way of leaving. 
    Weird, you think to yourself...

    Next to you, there is a table with a book and a half empty mug on top, below you is an old looking rug,
    and in front of you is another door.
    What will you do next?

    > door
    You try to open the door in front of you but it is closed shut

    > check rug
    You notice that you are standing on an old and dusty looking rug.
    After remembering how in movies most protagonists are stupid enough to put their keys under their entrance rug, 
    which is a very dumb trope that movies should stop to use. It is ridiculous, how did they get away with it for so long, it is always used as a plot developement device when it is such a stupid and uncommon thing to do. A kid would figure this out. 
    Anyway, after checking under it you find a key, as you expected. Dissapointing.

    > door
    Wowzers, it worked! As you slowly open the door you find your friend sitting on his couch watching TV.
    When you asked him how he warped inside, he told you casually that he just entered while you took a stupid picture.
    You then ask him why you can't open the door without its key when your inside, and he just tells you that it is a security measure.
    You then proceed to criticize him for putting his second door's key under a rug and about his book taste (even if you don't know what the book was even about) and that's it, you escaped, kind of.


    >>> escape_room()
    You were walking with a friend towards his house. In front of it you find a beautiful ladybug and proceed to take a picture of it. 
    When you turn around, you couldn't find your friend.
    You assume he entered while you were busy, so upon opening the main door, you found a narrow room.
    When you enter the room,  the door behind you closes shut and you have no way of leaving. 
    Weird, you think to yourself...

    Next to you, there is a table with a book and a half empty mug on top, below you is an old looking rug,
    and in front of you is another door.
    What will you do next?

    > rug
    You notice that you are standing on an old and dusty looking rug.
    After remembering how in movies most protagonists are stupid enough to put their keys under their entrance rug, 
    which is a very dumb trope that movies should stop to use. It is ridiculous, how did they get away with it for so long, it is always used as a plot developement device when it is such a stupid and uncommon thing to do. A kid would figure this out. 
    Anyway, after checking under it you find a key, as you expected. Dissapointing.

    > key
    Wowzers, it worked! As you slowly open the door you find your friend sitting on his couch watching TV.
    When you asked him how he warped inside, he told you casually that he just entered while you took a stupid picture.
    You then ask him why you can't open the door without its key when your inside, and he just tells you that it is a security measure.
    You then proceed to criticize him for putting his second door's key under a rug and about his book taste (even if you don't know what the book was even about) and that's it, you escaped, kind of.
    """
    key_is_found = False
   
    print("You were walking with a friend towards his house. In front of it you find a beautiful ladybug and proceed to take a picture of it. ")
    print("When you turn around, you couldn't find your friend.")
    print("You assume he entered while you were busy, so upon opening the main door, you found a narrow room.")
    print("When you enter the room,  the door behind you closes shut and you have no way of leaving. ")
    print("Weird, you think to yourself...\n")
    print("Next to you, there is a table with a book and a half empty mug on top, below you is an old looking rug,")
    print("and in front of you is another door.")
    print("What will you do next?")
   
    command = ""
    while key_is_found == False or "key" not in command.lower():
        command = input ("\n> ")
        if "list commands" in command.lower():
            print("examine table\npick up book\ncheck mug\nexamine rug\nopen door")
            
        elif "table" in command.lower():
            print("You approach the table in front of you, it is slightly dusty. You look at the book and the mug.")
        
        elif "book" in command.lower():
            print("When you pick up the book, you notice that it is called The Diary of Anne Frank, the synopsis reads as following:\nAnne Frank blablalballalblablalbla... too long for you to read so you give up after reading the first two words of the synopsis.")
            print("Since you immediately lost interest in it you put it back on the table and forget you even picked up a book.")
        
        elif "mug" in command.lower():
            print("As you approach the mug you notice that it is coffee, and when you pick it up you feel that it is still warm.")
            print("Since you love coffee you decide to give it a sip to judge its quality. ")
            print("mmm Nice, you say, as you take a warm sip. Since you do not want to be too disrespectful you put it back on the table (and take another sip before putting it back again)")
        elif "door" in command.lower():
            if key_is_found:
                victory_message()
                break
            else:
                print("You try to open the door in front of you but it is closed shut")       
            
        
        elif "rug" in command.lower():
            print("You notice that you are standing on an old and dusty looking rug.")
            print("After remembering how in movies most protagonists are stupid enough to put their keys under their entrance rug, ")
            print("which is a very dumb trope that movies should stop to use. It is ridiculous, how did they get away with it for so long,")
            print("it is always used as a plot developement device when it is such a stupid and uncommon thing to do. A kid would figure this out. ")
            print("Anyway, after checking under it you find a key, as you expected. Dissapointing.")
            key_is_found = True
        elif "key" in command.lower():
            if key_is_found:
                victory_message()
                break
            else:
                print("The only keys you have are yours and they don't work on this door (thankfully. it would have been alarming if they did)")
        else:
            print("You have entered an invalid command. Type list commands to see all the valid commands to type!")

    
   
   
   
   
   
   

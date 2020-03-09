#--------------------------------------
#Syd likes to procrastinate aka External Files Summative.
#Sydney Loerzel
#March 09, 2020
#--------------------------------------
#External files are good for this file in the case of you saving
#for the 'next game'. Aka ending I will never write.
#You save your inventory of bread and stats although its
#better not to save stats and load the default if it was a real game
#As well you are given the default start stats for Shooky. Saving the inventory
#externally uses less memory and having the data externally shortens the code.
#You don't have to input everything it is given and can be edited and saved.
#Disclaimer: I used a YouTube video as storyline inspiration for the code
#It is the Shooky video series of the BT21 universe.
#--------------------------------------

#---------------Lists------------------
user_details = {}

#-------------Functions----------------

def intro():
    print("'My name is Shooky. My grandpa is the best baker in town'")
    print("'It would be great if more people could taste grandpas bread'")
    print("'Oh! Look at the time! Lets head back to the bakery'")
    print("Shooky walks back to his grandpa's bakery")
    print("He walks in to find his grandpa laying on the ground")
    print("'Grandpa MUSTASHU!'")
    print("''Ugh...Shooky, Beware...Of the mil..k..''")
    print("Discovered[Sour Milk]")
    print("~A few days later~")
    print("''Shooky. Can you find us a baker that can continue the bakery on my behalf''")
    print("'A baker to replace you... Ok! I will!'")
    print("''Shooky. Life is about making choices. Have faith in you choices, always''")
    print("'Do not worry Grandpa. I will not let you down'")
    print("Now comes the journey to find a baker")
    print("You gather the CRUNCHY Squad to help. All your cookie friends.")
    print("You now control Shooky's actions")
    
def shooky_info():
    details = open('shooky.txt', 'r')
    user_profile = details.read().split(',') #splits at each comma, making a list
    print(user_profile) #shows that it is now in a list
    item = 0
    while item < (len(user_profile)): #turns the list into a dictionary
        user_details[user_profile[item]] = user_profile[item + 1]
        item = item + 2
    details.close() #closes the file
    return details #returns the file to be used in other functions
    
def find_bakers():
    print("You leave the bakery and begin looking for other bakers")
    print("The first two were easy to find and willing to come")
    print("The two bakers prepare bread for you")
    print("[Obtained: French Bread]")
    print("[Obtained: Pretzel]")
    file = open('inventory.txt', 'w') #opens the file to write mode
    file.write("French Bread,")
    file.write("Pretzel,")
    file.close() #closes the file
    return file
    
def duel():
    print("You are walking to find the third baker")
    print("[An Angry baker appeared]")
    print("He is not willing to help as easily...")
    print("He initiates a duel")
    print("[Baker HP: 50 ]")
    print("[Baker Level: 100 ]")
    print("[Shooky HP:", user_details["HP"], "]")
    print("[Shooky Level:", user_details["Level"], "]")
    print("He attacks first with water")
    print("[Baker used Mist]")
    print("[Mist wasn't effective")
    print("[Shooky loses 5 health]")
    user_details["HP"] = "55" #Lowers HP
    print("Your turn to fight")
    print("You use your only option, Tell Sad Story")
    print("'With Grandpa sick...How will I feed these many CRUNCHY Squad mouths'")
    print("'Sniff...Sniff...' You add sniffling on tears")
    print("[Shooky used Tell Sad Story]")
    print("[It's super effective]")
    print("[Gotcha! Baker was caught]")

def third_bread():
    print("The third baker prepares some plain white bread for you")
    file1 = open('inventory.txt', 'a') #opens file in append mode to add to it
    file1.write("Bread")
    file1.close()
    return file1 #Returns file now that we are done using it for now.
    
def ending():
    print("You start to walk home with the bread")
    print("You are going to let Grandpa Mustachu taste test")
    print("He'll choose who takes over his bakery")
    print("You now see the credit screen and no longer have control of Shooky")
    print("You don't know the ending. It says there will be a game two")
    print("But who knows when you'll be able to come back to the story")
    print("You'll need the inventory from this game and stats")
    print("Shooky's stats appear on screen")
    print(user_details)
    choice = input("Would you like to save your data? type 'y' for yes or 'n' for no")
    if choice == "y":
        print("Saving")
        with open ('shooky.txt', 'w') as f: #opens the file and closes when done working with it
            for akey in user_details.keys(): #goes through keys spliting apart the key and value
                f.write(akey + ",") #writes the key plus a comma
                f.write((user_details[akey])) #writes the value after that goes with the key previously
                if akey != "HP":
                    f.write(",") #Adds a comma to the end unless it is the last one
        print("Thanks for playing")
        exit()
    elif choice == "n":
        print("Not saving")
        print("Thanks for playing")
        exit()
    
def main():
    intro()
    input("> ") #A space to catch up and read everything.
    shooky_info()
    find_bakers()
    input("> ")
    duel()
    third_bread()
    input("> ")
    ending()

#----------------Code------------------
main()
#Importing
import os
import sys
import random
import json
import time

#When its run
with open('data.json','r') as f:
    data = json.load(f)

if data["firstRun"] == False:
    name = data["name"]
    print(f"[BOT]: Welcome back to DuBot, {name}")
else:
    print("[BOT]: Welcome to DuBot.")
    print("[BOT: It appears this is your first time running this file.")
    print("[BOT]: What is your name?")
    name = input()

    data["name"] = name
    data["firstRun"] = False
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("[BOT]: To get a list of commands type 'help'.")
    print()

    

#Defining Functions:

# If you can't use the requests library, remove all the code below:
import requests
def api_test():
    url = 'https://api.truthordarebot.xyz/v1/truth'
    choice = requests.get(url).json()

    choiceType = choice['type']
    choiceID = choice['id']
    choiceRating = choice['rating']
    choiceQuestion = choice['question']

    print(f'{choiceType}\n{choiceQuestion}\nID: {choiceID} | Rating: {choiceRating}')
# ok stop removing code before it breaks ty

# some neat little computing animations, dunno why i added them but i like them and they look cool so yeah. if you want to add them anywhere yourself just call the function.
def compute_dots(text: str = 'Computing',sleep_time: str = 1):
    for x in range (0,5):  
        b = f"{text}" + "." * x
        print (b, end="\r")
        time.sleep(sleep_time)

def compute_line(text: str = 'Computing',sleep_time: str = 1):
    line_choices = ['|','/','-','\\']
    for x in range (0,4):  
        current_line = line_choices[x]
        b = f'{text} {current_line}'
        print (b, end="\r")
        time.sleep(sleep_time)


# i really love these little one or two liner functions bc they're just so simple and easy to code and they always work first try and they're just like little happy encouragement pills i can make whenever im sick of seeing error messages. - j :)
def shutdown():
    print("[BOT]: Shutting Down.")
    exit()

def restart():
    print()
    os.execv(sys.executable, ['python'] + sys.argv)

def gay():
    randomGay = random.randint(0,100)
    print(f"[BOT]: You are {randomGay}% gay.")

def furry():
    print(f'[BOT]: You are {random.randint(0,100)}% furry.')

def love():
    print('Whos the first person?\n')
    person_one = input()
    print('Whos the second person?\n')
    person_two = input()
    
    compute_line(sleep_time=0.5)

    print(f'{person_one} and {person_two} are {random.randint(0,100)}% compatible.')

def say():
    print("[BOT]: What's the message?")
    message = input()
    print()
    print(message)

def coinflip():
    coin = ['Heads','Tails']
    result = random.choice(coin)
    print(f"[BOT]: The coin landed {result}.")

def dice():
    result = random.randint(1,6)
    print(f"[BOT]: The dice rolled {result}.")

def idea():
    print('if you have any ideas for this program, please message me on Discord at:\nDuzo#1010\n:)')

def list_data():
    firstRun = data['firstRun']
    username = data['name']
    compute_line('Processing data',1) # this doesnt do anything except do the animation i like
    print('Data:')
    compute_dots('First run : ',0.25) # once again, nothing just i like it
    print(f'First run : {firstRun}')
    compute_dots('Name : ',0.5) # you get the idea by now hopefully
    print(f'Name : {username}')

def rps():
    choices = ['rock','paper','scissors']

    print("[BOT]: Player 1, Pick rock, paper or scissors.")
    player_one = input().lower()
    i = 0
    while i < 25:
        print('\n')
        i = i + 1
    
    print("[BOT]: Player 2, Pick rock, paper or scissors.")
    player_two = input().lower()



    if player_one not in choices or player_two not in choices:
        print(f"[BOT]: One choice is incorrect. Please choose between Rock, Paper and Scissors.")
        return
    else:
        if player_two == player_one:
            print(f"[BOT]: Tie. {player_one} vs {player_two}")
            return
        elif player_two == "rock":
            if player_one == "paper":
                print(f"[BOT]: Player one wins! {player_one} vs {player_two}")
                return
            elif player_one == "scissors":
                print(f"[BOT]: Player two wins! {player_one} vs {player_two}")
                return
        elif player_two == "paper":
            if player_one == "scissors":
                print(f"[BOT]: Player one wins! {player_one} vs {player_two}")
                return
            elif player_one == "rock":
                print(f"[BOT]: Player two wins! {player_one} vs {player_two}")
                return
        elif player_two == "scissors":
            if player_one == "rock":
                print(f"[BOT]: Player one wins! {player_one} vs {player_two}")
                return
            elif player_one == "paper":
                print(f"[BOT]: Player two wins! {player_one} vs {player_two}")
                return

def rps_bot():
    choices = ['rock','paper','scissors']

    print("[BOT]: Pick rock, paper or scissors.")
    answer = input().lower()
    computerAnswer = random.choice(choices)


    if answer not in choices:
        print(f"[BOT]: {answer} is incorrect. Please choice between Rock, Paper and scissors.")
        return
    else:
        if computerAnswer == answer:
            print(f"[BOT]: Tie, you both chose {answer}.")
            return
        elif computerAnswer == "rock":
            if answer == "paper":
                print(f"[BOT]: You win! The computer chose {computerAnswer}.")
                return
            elif answer == "scissors":
                print(f"[BOT]: You lose. The computer chose {computerAnswer}.")
                return
        elif computerAnswer == "paper":
            if answer == "scissors":
                print(f"[BOT]: You win! The computer chose {computerAnswer}.")
                return
            elif answer == "rock":
                print(f"[BOT]: You lose. The computer chose {computerAnswer}.")
                return

        elif computerAnswer == "scissors":
            if answer == "rock":
                print(f"[BOT]: You win! The computer chose {computerAnswer}.")
                return
            elif answer == "paper":
                print(f"[BOT]: You lose. The computer chose {computerAnswer}.")
                return
        
def nguess():
    print("[BOT]: What's your number? 1-10")
    number = input()

    correctNumber = random.randint(1,10)

    if number == correctNumber:
        print(f"[BOT]: You win! {number} was the correct number.")
        return
    else:
        print(f"[BOT]: You lose. {correctNumber} was the correct number.")
        return


def yn():
    responses = ['Yes','No']

    print("[BOT]: What's your question?")
    question = input()
    answer = random.choice(responses)

    print(f"[BOT]: Question: {question}")
    print(f"[BOT]: Answer: {answer}")

def e():
    eList = ''
    eAmount = random.randint(1,10000)
    while 0 < eAmount:
        eList = eList + "e"
        eAmount = eAmount - 1
    print(eList)

def ball():
    responses = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"]

    print("[BOT]: What's the question?")
    question = input()
    answer = random.choice(responses)

    print(f"[BOT]: Question: {question}")
    print(f"[BOT]: Answer: {answer}")

def info():
    print("[BOT]: Based off of DuBot (https://discord.com/api/oauth2/authorize?client_id=865190020179296267&permissions=93184&scope=bot)")
    print("[BOT]: Created in Python")
    print("[BOT]: Created by James Hall (Duzo)")

spaceWeights_planets = {
    "sun": 27.01,
    "mercury": 0.38,
    "venus": 0.91,
    "moon": 0.166,
    "mars": 0.38,
    "jupiter": 2.34,
    "saturn": 1.06,
    "uranus": 0.92,
    "neptune": 1.19,
    "pluto": 0.06,
    "earth": 1,
    "io": 0.183,
    "europa": 0.133,
    "ganymede": 0.144,
    "callisto": 0.126
}

def spaceweights():
    try:
        print("[BOT]: What's your weight in KG?")
        weight = (int(input()) / 9.81)
        print()

        print("[BOT]: What planet?")
        chosen_planet = input().lower()
        if chosen_planet not in spaceWeights_planets:
            planetList = ""
            for val in spaceWeights_planets:
                planetList = planetList + val + "\n"
            return print(f"Please provide a valid planet:\n{planetList}")

        planetWeight = spaceWeights_planets[chosen_planet] * weight
        
        print(f'Your weight on {chosen_planet} is {planetWeight}')
    except Exception as error:
        print(f'An error occured!\n{error}')

    
    
def changename():
    print("[BOT]: What is your new name?")
    newName = input()
    data["name"] = newName
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("[BOT]: Complete.")

def datareset():
    
    print("[BOT]: Are you sure you wish to reset all data?")
    dataChoice = input().lower()
    if dataChoice == "yes":
        data["firstRun"] = 1
        data["name"] = None
        with open('data.json','w') as f:
            json.dump(data, f, indent=4)
        print("[BOT]: Data reset complete.")
        restart()
    else:
        print("[BOT]: Cancelling data reset.")
        return
    

def help():
    print("[BOT]: ")
    print("Help:")
    print("Shutdown: Shuts this down")
    print("Restart: Restarts this")
    print("Say: Repeats your message")
    print("CoinFlip: Flips a coin")
    print("Dice: Rolls a dice")
    print("RPS: Play rock paper scissors against someone")
    print("rps_bot: Play rock paper scissors against the code")
    print("NGuess: Play a number guessing game")
    print("Gay: Tells you how gay you are")
    print("YN: Answers your questions with Yes or No")
    print("Ball: The 8ball answers your questions.")
    print("Info: Info on this thing")
    print("SpaceWeights: Gives your weight on other planets.")
    print("ChangeName: Let's you change your name.")
    print("DataReset: Resets all your data.")
    print("Help: This command")
    print('E: e')
    print('api_test: if it crashes when you run this then u got no requests library installed.')
    print('idea - give me ideas please')
    print('love: see how compatible two people are')
    print('furry: how much of a furry are you?')


def main():
    print()
    #print("What's the command?")
    command = input().lower()
    
    method_name = command
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(method_name)
    if not method:
        print('That command does not exist.')
        return
    method()

#The loop:

while True:
    main()
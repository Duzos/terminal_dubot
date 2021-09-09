#Importing
import os
import sys
import random
import json

#When its run
with open('data.json','r') as f:
    runCheck = json.load(f)

if runCheck["firstRun"] == 0:
    name = runCheck["name"]
    print(f"[BOT]: Welcome back to DuBot, {name}")
else:
    runCheck["firstRun"] = 1
    
    print("[BOT]: Welcome to DuBot.")
    print("[BOT: It appears this is your first time running this file.")
    print("[BOT]: What is your name?")
    name = input()

    runCheck["name"] = name
    runCheck["firstRun"] = 0
    with open('data.json', 'w') as f:
        json.dump(runCheck, f, indent=4)

    print("[BOT]: To get a list of commands type 'help'.")
    print()

    
# print("Welcome to Dubot but without the bot part.")
# print("Press enter to begin.")
# input()

#Defining Functions:

def shutdown():
    print("[BOT]: Shutting Down.")
    exit()

def restart():
    print()
    os.execv(sys.executable, ['python'] + sys.argv)


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

def rps():
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

def gay():
    randomGay = random.randint(0,100)
    print(f"[BOT]: You are {randomGay}% gay.")

def yn():
    responses = ['Yes','No']

    print("[BOT]: What's your question?")
    question = input()
    answer = random.choice(responses)

    print(f"[BOT]: Question: {question}")
    print(f"[BOT]: Answer: {answer}")

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

def spaceWeights():
    print("[BOT]: What's your weight in KG?")
    weight = (int(input()) / 9.81)
    print()

    print("[BOT]: What planet?")
    planet = input().lower()

    if planet == "moon":
        print(f"[BOT]: Your weight on the Moon is {round(weight * 1.622)} kg")
        return
    elif planet == "mars":
        print(f"[BOT]: Your weight on Mars is {round(weight * 3.711)} kg")
        return
    elif planet == "venus":
        print(f"[BOT]: Your weight on Venus is {round(weight * 8.87)} kg")
        return
    elif planet == "mercury":
        print(f"[BOT]: Your weight on Mercury is {round(weight * 3.7)} kg")
        return
    elif planet == "saturn":
        print(f"[BOT]: Your weight on Saturn is {round(weight * 10.44)} kg")
        return
    elif planet == "neptune":
        print(f"[BOT]: Your weight on Neptune is {round(weight * 11.15)} kg")
        return
    elif planet == "uranus":
        print(f"[BOT]: Your weight on Uranus is {round(weight * 8.69)} kg")
        return
    elif planet == "jupiter":
        print(f"[BOT]: Your weight on Jupiter is {round(weight * 24.79)} kg")
        return
    
def changeName():
    with open('data.json','r') as f:
        nameChange = json.load(f)

    print("[BOT]: What is your new name?")
    newName = input()
    nameChange["name"] = newName
    with open('data.json', 'w') as f:
        json.dump(nameChange, f, indent=4)
    print("[BOT]: Complete.")

def dataReset():
    with open('data.json','r') as f:
        resetData = json.load(f)
    
    print("[BOT]: Are you sure you wish to reset all data?")
    dataChoice = input().lower()
    if dataChoice == "yes":
        resetData["firstRun"] = 1
        resetData["name"] = None
        with open('data.json','w') as f:
            json.dump(resetData, f, indent=4)
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
    print("RPS: Play rock paper scissors")
    print("NGuess: Play a number guessing game")
    print("Gay: Tells you how gay you are")
    print("YN: Answers your questions with Yes or No")
    print("Ball: The 8ball answers your questions.")
    print("Info: Info on this thing")
    print("SpaceWeights: Gives your weight on other planets.")
    print("ChangeName: Let's you change your name.")
    print("DataReset: Resets all your data.")
    print("Help: This command")


def main():
    print()
    #print("What's the command?")
    command = input().lower()
    
    if command == "shutdown":
        shutdown()
    elif command == "restart":
        restart()
    elif command == "say":
        say()
    elif command == "coinflip":
        coinflip()
    elif command == "dice":
        dice()
    elif command == "rps":
        rps()
    elif command == "nguess":
        nguess()
    elif command == "gay":
        gay()
    elif command == "yn":
        yn()
    elif command == "ball":
        ball()
    elif command == "info":
        info()
    elif command == "spaceweights":
        spaceWeights()
    elif command == "changename":
        changeName()
    elif command == "datareset":
        dataReset()
    elif command == "help":
        help()

#The loop:

while True:
    main()
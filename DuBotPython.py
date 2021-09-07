#Importing
import os
import sys
import random

from discord.ext.commands.errors import CommandNotFound

#When its run
print("Welcome to Dubot but without the bot part.")
print("Press enter to begin.")
input()

#Defining Functions:

def shutdown():
    print("Shutting Down.")
    exit()

def restart():
    print()
    os.execv(sys.executable, ['python'] + sys.argv)


def say():
    print("What's the message?")
    message = input()
    print()
    print(message)

def coinflip():
    coin = ['Heads','Tails']
    result = random.choice(coin)
    print(f"The coin landed {result}.")

def dice():
    result = random.randint(1,6)
    print(f"The dice rolled {result}.")

def rps():
    choices = ['rock','paper','scissors']

    print("Pick rock, paper or scissors.")
    answer = input().lower()
    computerAnswer = random.choice(choices)


    if answer not in choices:
        print(f"{answer} is incorrect. Please choice between Rock, Paper and scissors.")
        return
    else:
        if computerAnswer == answer:
            print(f"Tie, you both chose {answer}.")
            return
        elif computerAnswer == "rock":
            if answer == "paper":
                print(f"You win! The computer chose {computerAnswer}.")
                return
            elif answer == "scissors":
                print(f"You lose. The computer chose {computerAnswer}.")
                return
        elif computerAnswer == "paper":
            if answer == "scissors":
                print(f"You win! The computer chose {computerAnswer}.")
                return
            elif answer == "rock":
                print(f"You lose. The computer chose {computerAnswer}.")
                return

        elif computerAnswer == "scissors":
            if answer == "rock":
                print(f"You win! The computer chose {computerAnswer}.")
                return
            elif answer == "paper":
                print(f"You lose. The computer chose {computerAnswer}.")
                return
        
def nguess():
    print("What's your number? 1-10")
    number = input()

    correctNumber = random.randint(1,10)

    if number == correctNumber:
        print(f"You win! {number} was the correct number.")
        return
    else:
        print(f"You lose. {correctNumber} was the correct number.")
        return

def gay():
    randomGay = random.randint(1,100)
    print(f"You are {randomGay}% gay.")

def yn():
    responses = ['Yes','No']

    print("What's your question?")
    question = input()
    answer = random.choice(responses)

    print(f"Question: {question}")
    print(f"Answer: {answer}")

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

    print("What's the question?")
    question = input()
    answer = random.choice(responses)

    print(f"Question: {question}")
    print(f"Answer: {answer}")

def info():
    print("Based off of DuBot (https://discord.com/api/oauth2/authorize?client_id=865190020179296267&permissions=93184&scope=bot)")
    print("Created in Python")
    print("Created by James Hall (Duzo)")

def help():
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
    print("Help: This command")


def main():
    print("What's the command?")
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
    elif command == "help":
        help()

#The loop:

while True:
    main()
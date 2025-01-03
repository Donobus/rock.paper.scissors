import random

import time

choices = ["rock", "paper", "scissors"]
joke_answers = ["gun", "grenade", "bomb", "nuke", "nuclear", "magic", "wizard"]
yes_answers = ["yes", "yeah", "sure", "ok", "okay", "yup", "yep" "play", "again", "rematch", "another", "change", "mind"]
no_answers = ["no", "don't", "not", "stop", "quit", "end", "exit", "leave", "done", "finish", "nope", "nah", "naw", "negative", "not", "no way", "nope", "no thanks", "no thank you", "no sir", "no ma'am", "no mam", "dont", "wont"]

while True:
    print("")
    user_choice = input("Rock, paper, scissors, shoot! ").lower()
    computer_choice = random.choice(choices)

    print(f"You chose {user_choice}, computer chose {computer_choice}.")

    time.sleep(2)
    
    if any(joke_answer in user_choice for joke_answer in joke_answers):
        print("Cheater! I'm not playing anymore!")
        cheater_response = input("").lower()

        while True:
            if  "please" in cheater_response
                del cheater_response
                print(".....")
                time.sleep(4)
                print("Fine, I guess I'll play again.")
                time.sleep(2)
                break

            else:
                print("...")
                time.sleep(7)
                print("Maybe if you asked me nicely...")
                cheater_response = input("").lower()

        continue

    elif user_choice == computer_choice:
        print("It's a tie!")
        time.sleep(2)
        print("Let's go again!")
    
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("""You win! I want a rematch!""")
        time.sleep(2)

    
    elif user_choice not in choices:
        print("I don't think you quite know how to play this game.")
        time.sleep(3)
        print("""
...""")
        time.sleep(5)
        print("""

.....""")
        time.sleep(8)
        print("""

              
Let's try this again...
""")
        time.sleep(2)

    else:
        print("You lose!")
        time.sleep(2)
        lose_response = input("Want to go again? ").lower()
        rematch = True
        
        while True:

            if any(yes_answer in lose_response for yes_answer in yes_answers)
                rematch = True
                print("Great! Let's play again!")
                time.sleep(2)
                break

            elif rematch == False:
                lose_response = input("").lower()

            else:
                print("Guess it's better to quit while I'm ahead anyway. Let me know if you change your mind!")
                lose_response = input("").lower()
                rematch = False
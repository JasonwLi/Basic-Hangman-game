##
##  Created by Jason Li on 2016-11-19.
##  Copyright © 2016 JasonwLi. All rights reserved.




# String constants for interactive game of hangman    
letter_prompt = "Enter your choice of letter: "
used_message = "Letter previously guessed "
incorrect_message = "Incorrect guess"
win_message = "You won! The word was {0}"
lose_message = "You lose! The word was {0}"
current_message = "Target: {0}. Missed letters: {1}"



def play_hangman(secret, max_misses):
    target = "-" * len(secret)
    guess = ""
    missed = ""
    while not (max_misses == 0) and not (secret == target):
        counter = 0
        print(current_message.format(target, missed))
        guess = input(letter_prompt)
        if target.find(guess) != -1 or missed.find(guess) != -1:
            print(used_message)
        elif secret.find(guess) != -1:
            while counter < len(secret):
                if guess == secret[counter]:
                    target = target[:counter] + guess + target[counter+1:]
                    counter += 1
                else:
                    counter += 1
        else:
            missed = missed+guess
            max_misses -= 1
            print(incorrect_message)
    if secret == target:
        print(win_message.format(secret))
    elif max_misses == 0:
        print(lose_message.format(secret))
    

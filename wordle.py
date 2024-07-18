import os
import random

words = [
    "Apple", "Bread", "Chase", "Dream", "Eagle", "Flame", "Grace",
    "Heart", "Ivory", "Jewel", "Knife", "Light", "Maple", "North",
    "Olive", "Peace", "Quest", "River", "Stone", "Trust"
]

target_word = random.choice(words)

def get_feedback(guess, target):
    feedback = []
    for i in range(len(guess)):
        if guess[i] == target[i]:
            feedback.append(f'\033[92m{guess[i]}\033[0m')  # Green for correct letter in the correct position
        elif guess[i] in target:
            feedback.append(f'\033[33m{guess[i]}\033[0m')
        else:
            feedback.append(f'\033[91m{guess[i]}\033[0m')  # Red for incorrect letter
    return ''.join(feedback)


def wordle():
    os.system('cls')
    print(' ___       __   ________  ________  ________  ___       _______      ')
    print('|\  \     |\  \|\   __  \|\   __  \|\   ___ \|\  \     |\  ___ \     ')
    print('\ \  \    \ \  \ \  \|\  \ \  \|\  \ \  \_|\ \ \  \    \ \   __/|    ')
    print(' \ \  \  __\ \  \ \  \ \  \ \   _  _\ \  \ \  \ \  \    \ \  \_|/__  ')
    print('  \ \  \|\__\_\  \ \  \ \  \ \   \   \ \  \_ \ \ \  \____\ \  \_|\ \ ')
    print('   \ \____________\ \_______\ \__\  _ \ \_______\ \_______\ \_______')
    print('    \|____________|\|_______|\|__|\|__|\|_______|\|_______|\|_______|')
    print('')
    print('[>] Created By   : ebola-cmd')
    print('[>] Version      : 1.0')
    print('')
    print('[!] What do you want to do? :')
    print('')
    print('[1] Play')
    print('[2] Tutorial')
    print('[3] Exit')
    c_1 = input('[>] ')
    if c_1 == "1":
        game()
        
    if c_1 == "2":
        tutorial()
        
    if c_1 == "3":
        exit()
        
def game():
    os.system('cls')
    attempts = 6
    print('[!] Enter a 5-letter word')
    for attempt in range(1, attempts + 1):
        guess = input(f"[{attempt}] ").lower()
        
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        
        feedback = get_feedback(guess, target_word)
        print('[>]', feedback)
        
        if guess == target_word:
            input("Congratulations! You've guessed the word!")
            wordle()
        
    input(f"Sorry, you've used all your attempts. The word was: {target_word}")
    wordle()
    
def tutorial():
    os.system('cls')
    print('[!] How to play')
    print('[!] Guess the word in 6 tries')
    print('[>] Each guess must be a valid 5-letter word.')
    print('[>] The color of the tiles will change to show how close your guess was to the word.')
    print('')
    print('[Examples:]')
    print('\033[92mW\033[0mEARY')
    print('W is in the word and in the correct spot.')
    print('')
    print('P\033[93mI\033[0mLLS')
    print('I is in the word but in the wrong spot.')
    print('')
    print('VAGUE')
    print('No letter is in the word')
    print('')
    print('press any key...')
    input('[>]')
    wordle()
    
def exit():
    print('See you some other time...')

wordle()
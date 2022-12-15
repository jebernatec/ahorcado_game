import random
import os

lifes = 6
writed_words = []

def select_group():

    global list_group
    
    with open("groups.txt") as group:
        list_group = [gr.rstrip() for gr in group]
    
    print("select a category:")
    for i, gr in enumerate(list_group):
        print(f"{i+1}. {gr}")

    return int(input(">>>")) - 1

def select_word(s_g):
    
    with open(list_group[s_g] + ".txt") as s_group:
        list_words = [wrd.rstrip() for wrd in s_group]
    
    word_select = random.choice(list_words)

    return word_select

def word_maker(w_s):
    global list_word

    list_word = []

    for letter in w_s:
        list_word.append({
            "letter": letter,
            "guessed": False
        })

def show_word():
    
    for letter in list_word:
        if letter["guessed"]:
            print(letter[" letter "], end="")
        else:
            print(" _ ", end="")
        
    print("")

def show_ahorcado():
    if lifes == 1:
        print("""
                       ___
                      |   |
                      O   |
                     /|\  |
                     / \  |
                    ______|
        """)
    elif lifes == 2:
        print("""
                       ___
                      |   |
                      O   |
                     /|\  |
                       \  |
                    ______|
        """)
    elif lifes == 3:
        print("""
                       ___
                      |   |
                      O   |
                     /|\  |
                          |
                    ______|
        """)
    elif lifes == 4:
        print("""
                       ___
                      |   |
                      O   |
                      |\  |
                          |
                    ______|
        """)
    elif lifes == 5:
        print("""
                       ___
                      |   |
                      O   |
                      |   |
                          |
                    ______|
        """)
    elif lifes == 6:
        print("""
                       ___
                      |   |
                      O   |
                          |
                          |
                    ______|
        """)

def discover_word(letter):

    if letter in writed_words:
        return
    else:
        writed_words.append(letter)

    if not letter_is_in_word(letter):
        lifes -=1
    else:
        for l in list_word:
            if l["letter"] == letter:
                l["guessed"] = True

def letter_is_in_word(l):

    for letter in list_word:
        if letter["letter"] == l:
            return True
    return False
    

def main():
    s_g = select_group()
    w_s = select_word(s_g)
    word_maker(w_s)
    show_ahorcado()
    show_word()
    discover_word(input("enter a letter >>> "))

    if lifes <=0:
        print("you lost, the word was", w_s)
        return
    if win():
        print("victory")
        return

    

main()



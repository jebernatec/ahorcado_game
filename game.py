import random
import os


def select_group():
    
    with open("grupos.txt") as group:
        list_group = [gr.rstrip() for gr in group]
    
    print("select a category:")
    for i, gr in enumerate(list_group):
        print(f"{i+1}. {gr}")

    return int(input("-->"))


def main():
    select_group()


main()



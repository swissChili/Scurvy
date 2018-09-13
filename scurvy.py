#!/usr/bin/python3
import sys

file = sys.argv[1]

with open(file, "r") as d:
    deck = d.read()
    d.close()

cards = deck.split("\n")

for iter, i in enumerate(cards):
    cards[iter] = i.split(":")

def show_card(card, front):
    print(chr(27) + "[2J")
    print("\u001b[45m\n\n\n")
    if front == True:
        print(card[0])
    else:
        print(card[-1])
    print("\n\n  \u001b[0m\n")

current_card = 0
front = True
def loop_input(current_card, front, deck):
    if front == True:
        side = "front"
    else:
        side = "back"
    print("Card {card} of {total}. {side}".format(card = current_card, total = len(deck), side = side))
    i = input("vi keys:\n")
    if i == "l":
        current_card += 1
        front = True
    elif i == "h":
        current_card -= 1
        front = True
    elif i == "k" or i == "j":
        front = not front
    show_card(cards[current_card], front)
    loop_input(current_card, front, deck)
show_card(cards[0], True)
loop_input(current_card, front, cards)

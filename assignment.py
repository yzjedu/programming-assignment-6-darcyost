# Programmer: [Darcy Ostrander]
# Course: CS701/GB-731, Dr. Yalew
# Date: [8/21/2024]
# Programming Assignment: 6
# Program Inputs: 
# Program Outputs: Random BlackJack hand and value of hand

import random

# Function that generates a shuffled deck of 52 cards.
def generate_deck():
    suits = ["h", "d", "c", "s"]
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
    deck = []
    for suit in suits:
        for value in values:
            deck.append(value + suit)
    random.shuffle(deck)
    return deck
    
# Function that returns the name of a card given its string representation.
def card_name(card):
    name = ""
    # numbers
    if "13" in card:
        name = name + "King of "
    elif "12" in card:
        name = name + "Queen of "
    elif "11" in card:
        name = name + "Jack of "
    elif "10" in card:
        name = name + "10 of "
    elif "9" in card:
        name = name + "9 of "
    elif "8" in card:
        name = name + "8 of "
    elif "7" in card:
        name = name + "7 of "
    elif "6" in card:
        name = name + "6 of "
    elif "5" in card:
        name = name + "5 of "
    elif "4" in card:
        name = name + "4 of "
    elif "3" in card:
        name = name + "3 of "
    elif "2" in card:
        name = name + "2 of "
    elif "1" in card:
        name = name + "Ace of "
    else:
        print("That card does not exist")
        exit()
    # suits
    if "h" in card:
        name = name + "Hearts"
    elif "s" in card:
        name = name + "Spades"
    elif "d" in card:
        name = name + "Diamonds"
    elif "c" in card:
        name = name + "Clubs"
    else:
        print("That card does not exist")
        exit()
    return name

# Function that displays the names of the cards in a hand.
def display_hand(hand):
    for card in hand:
        print(card_name(card))

# Function that calculates and returns the total value of a hand.

def hand_value(hand):
    sum = 0
    for card in hand:
        val = card.split("d")[0]
        val = val.split("c")[0]
        val = val.split("s")[0]
        val = val.split("h")[0]
        val = int(val)
        if val >= 10:
            val = 10
        sum = sum + val
    for card in hand:
        val = card.split("d")[0]
        val = val.split("c")[0]
        val = val.split("s")[0]
        val = val.split("h")[0]
        val = int(val)
        if val == 1 and (sum + 10 <= 21):
            sum = sum + 10
    print(sum)
    return sum


def main():
    # Write the code for the main function here and delete pass
    deck = generate_deck()
    hand = []
    hand.append(deck.pop())
    hand.append(deck.pop())
    display_hand(hand)
    playerval = hand_value(hand)
    dealerHand = []
    dealerHand.append(deck.pop())
    dealerHand.append(deck.pop())
    dealerval = hand_value(dealerHand)
    print("dealer:" + str(dealerval))
    if dealerval > playerval and dealerval <=21:
        print("dealer wins")
    elif playerval > dealerval and playerval <=21:
        print("player wins")
    else:
        print("no one wins")
    
    



if __name__ == "__main__":
    main()
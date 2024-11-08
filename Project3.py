"""
The Decktet is a non-standard deck that consists of 37 cards of value 1-10
in 6 suits. Many cards have two suits, and one card ("The Excuse") has no
suit or value. Your job is to define a new poker-type game that uses this
deck in which a player is dealt four cards to form a hand. Determine
the possible winning hands and the payout a player receives for each hand.
Then determine the price the player pays for losing a hand and compute
the full expected value for this game from the player's perspective. As
part of this assignment, you must decide how to treat the Excuse card.
"""

#our hands:
# 1. 4-suited hand
# 2. Matching Suit Ace and Crown
# 3. Straight
# 4. Pair
# 5. 3 Crowns and Excuse

from itertools import combinations

class Card:
    def __init__(self, name, value, suits):
        self.name = name
        self.value = value
        self.suits = suits

    def __repr__(self):
        return f"{self.name} ({self.value}, {self.suits})"

# Define the Decktet deck
deck = [
    #single suit cards
    Card("Ace of Moons", 1, ["Moons"]),
    Card("Crown of Moons", 10, ["Moons"]),
    Card("Ace of Suns", 1, ["Suns"]),
    Card("Crown of Suns", 10, ["Suns"]),
    Card("Ace of Waves", 1, ["Waves"]),
    Card("Crown of Waves", 10, ["Waves"]),
    Card("Ace of Leaves", 1, ["Leaves"]),
    Card("Crown of Leaves", 10, ["Leaves"]),
    Card("Ace of Wyrms", 1, ["Wyrms"]),
    Card("Crown of Wyrms", 10, ["Wyrms"]),
    Card("Ace of Knots", 1, ["Knots"]),
    Card("Crown of Knots", 10, ["Knots"]),

    #double suit cards
    Card("Two of Knots and Moons", 2, ["Knots", "Moons"]),
    Card("Two of Waves and Leaves", 2, ["Waves", "Leaves"]),
    Card("Two of Suns and Wyrms", 2, ["Suns", "Wyrms"]),

    Card("Three of Knots and Suns", 3, ["Knots", "Suns"]),
    Card("Three of Leaves and Wyrms", 3, ["Leaves", "Wyrms"]),
    Card("Three of Moons and Waves", 3, ["Moons", "Waves"]),

    Card("Four of Knots and Wyrms", 4, ["Knots", "Wyrms"]),
    Card("Four of Leaves and Waves", 4, ["Leaves", "Waves"]),
    Card("Four of Moons and Suns", 4, ["Moons", "Suns"]),

    Card("Five of Knots and Wyrms", 5, ["Knots", "Wyrms"]),
    Card("Five of Suns and Waves", 5, ["Suns", "Waves"]),
    Card("Five of Moons and Leaves", 5, ["Moons", "Leaves"]),

    Card("Six of Suns and Wyrms", 6, ["Suns", "Wyrms"]),
    Card("Six of Moons and Waves", 6, ["Moons", "Waves"]),
    Card("Six of Knots and Leaves", 6, ["Knots", "Leaves"]),

    Card("Seven of Knots and Suns", 7, ["Knots", "Suns"]),
    Card("Seven of Leaves and Moons", 7, ["Leaves", "Moons"]),
    Card("Seven of Waves and Wyrms", 7, ["Waves", "Wyrms"]),

    Card("Eight of Suns and Moons", 8, ["Suns", "Moons"]),
    Card("Eight of Knots and Wyrms", 8, ["Knots", "Wyrms"]),
    Card("Eight of Leaves and Waves", 8, ["Leaves", "Waves"]),

    Card("Nine of Knots and Leaves", 9, ["Knots", "Leaves"]),
    Card("Nine of Suns and Moons", 9, ["Suns", "Moons"]),
    Card("Nine of Wyrms and Waves", 9, ["Wyrms", "Waves"]),

    Card("The Excuse", -1, [])
]

def iterate_hands(deck):
    for hand in combinations(deck, 4):
        yield hand

def is_4_suited(hand):
    suits = set()
    for card in hand:
        suits.update(card.suits)
    return len(suits) == 4

def is_matching_suit_ace_and_crown(hand):
    ace = False
    crown = False
    for card in hand:
        if card.name.startswith("Ace"):
            ace = True
        elif card.name.startswith("Crown"):
            crown = True
    
    #check if the ace and crown are the same suit
    suitset = set()
    if ace and crown:
        for card in hand:
            if card.name.startswith("Ace") or card.name.startswith("Crown"):
                suitset.update(card.suits)
        if len(suitset) == 1:
            return True
    else:
        return False

def is_straight(hand):
    #handle unvalued excuse card
    values = sorted([card.value for card in hand])
    return values[0] == values[1] - 1 == values[2] - 2 == values[3] - 3

def is_pair(hand):
    values = [card.value for card in hand]
    return len(set(values)) == 3

def is_3_crowns_and_excuse(hand):
    crowns = 0
    excuse = False
    for card in hand:
        if card.name.startswith("Crown"):
            crowns += 1
        elif card.name == "The Excuse":
            excuse = True
    return crowns == 3 and excuse

if __name__ == "__main__":
    #run through the combinations to find probabilities of each hand
    total_hands = 0
    total_4_suited = 0
    total_matching_ace_and_crown = 0
    total_straight = 0
    total_pair = 0
    total_3_crowns_and_excuse = 0
    no_hand = 0

    for hand in iterate_hands(deck):
        total_hands += 1
        if is_3_crowns_and_excuse(hand):
            total_3_crowns_and_excuse += 1
        elif is_straight(hand):
            total_straight += 1
        elif is_matching_suit_ace_and_crown(hand):
            total_matching_ace_and_crown += 1
        elif is_pair(hand):
            total_pair += 1
        elif is_4_suited(hand):
            total_4_suited += 1
        else:
            no_hand += 1


        
    print(f"Total hands: {total_hands}")
    print(f"4-suited: {total_4_suited} ({total_4_suited/total_hands:.2%})")
    print(f"Matching suit ace and crown: {total_matching_ace_and_crown} ({total_matching_ace_and_crown/total_hands:.2%})")
    print(f"Straight: {total_straight} ({total_straight/total_hands:.2%})")
    print(f"Pair: {total_pair} ({total_pair/total_hands:.2%})")
    print(f"3 Crowns and Excuse: {total_3_crowns_and_excuse} ({total_3_crowns_and_excuse/total_hands:.2%})")
    print(f"No hand: {no_hand} ({no_hand/total_hands:.2%})")
    print("Total Reached" if sum([total_4_suited, total_matching_ace_and_crown, total_straight, total_pair, total_3_crowns_and_excuse, no_hand])==total_hands else "Incorrect Total")
    
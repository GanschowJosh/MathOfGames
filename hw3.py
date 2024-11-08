
"""
Euchre: You are playing a game that only uses the cards with values 9, 10, J, Q, K, and A from a
standard deck (therefore you have 24 total cards in the deck). In this game, each player is dealt
a hand of 5 cards
"""
def question1():
    """
    What is the expected number of suits you will have in your hand?
    """
    import itertools
    from collections import defaultdict
    print("\n========== Question 1 ==========")

    suits = ["H", "D", "C", "S"] # Hearts, Diamonds, Clubs, Spades

    deck = []
    for suit in suits:
        deck.extend([suit]*6) #represent each card by its suit
    
    total_hands = 0
    total_suits = 0

    suit_count_freq = defaultdict(int)

    for hand in itertools.combinations(deck, 5):
        total_hands += 1
        distinct_suits = len(set(hand))
        total_suits += distinct_suits
        suit_count_freq[distinct_suits] += 1
    
    expected_suits = total_suits / total_hands

    print(f"Total number of hands: {total_hands}")
    print(f"Total number of suits across all hands: {total_suits}")
    print(f"Expected number of suits per hand: {expected_suits:.4f}")

    """print("\nFrequency of distinct suits per hand:")
    for suit_count in sorted(suit_count_freq):
        frequency = suit_count_freq[suit_count]
        probability = frequency / total_hands
        print(f"{suit_count} suits: {frequency} hands ({probability:.4%})")"""

def question2():
    """
    Before dealing cards to each player, one card is turned face up in the middle of the table
    (and left there). The suit of this card is called the trump suit. What is the probability that
    you will have no trump cards? What is the probability you will have all trump cards?
    """
    import itertools
    print("\n========== Question 2 ==========")
    suits = ["H", "D", "C", "S"] # Hearts, Diamonds, Clubs, Spades

    trump_suit = "H"

    deck = []
    for suit in suits:
        if suit == trump_suit:
            deck.extend([suit]*5) #trump suit has 5 remaining cards
        
        else:
            deck.extend([suit]*6) #other suits have all 6 cards

    total_hands = 0
    no_trump_count = 0
    all_trump_count = 0

    non_trump_cards = [card for card in deck if card != trump_suit]
    trump_cards = [card for card in deck if card == trump_suit]

    total_combinations = itertools.combinations(deck, 5)

    for hand in itertools.combinations(deck, 5):
        total_hands += 1
        
        trump_in_hand = sum(1 for card in hand if card == trump_suit)

        if trump_in_hand == 0:
            no_trump_count += 1
        elif trump_in_hand == 5:
            all_trump_count += 1
        
    
    probability_no_trump = no_trump_count / total_hands
    probability_all_trump = all_trump_count / total_hands

    print(f"Total number of possible 5-card hands: {total_hands}")
    print(f"Number of hands with no trump cards: {no_trump_count}")
    print(f"Number of hands with all trump cards: {all_trump_count}\n")

    print(f"Probability of having no trump cards: {probability_no_trump:.4%}")
    print(f"Probability of having all trump cards: {probability_all_trump:.6%}")


"""
Abandon All Artichokes: Assume that you currently have 7 cards in your deck, 2 of which are
artichokes
"""
def question3():
    """
    If you shuffle your deck and draw 5 cards, what is the expected number of artichokes you will
    draw?
    """
    import itertools
    print("\n========== Question 3 ==========")
    artichokes = ["A1", "A2"]
    non_artichokes = ["N1", "N2", "N3", "N4", "N5"]
    deck = artichokes + non_artichokes

    total_hands = 0
    total_artichokes = 0

    for hand in itertools.combinations(deck, 5):
        total_hands += 1
        artichokes_in_hand = sum(1 for card in hand if card in artichokes)
        total_artichokes += artichokes_in_hand
    
    expected_artichokes = total_artichokes / total_hands

    print(f"Total number of possible 5-card hands: {total_hands}")
    print(f"Total number of artichokes across all hands: {total_artichokes}")
    print(f"Expected number of artichokes per hand: {expected_artichokes:.4f}")


def calculate_probability_zero_artichokes(deck, num_draw=5):
    """
    You have a choice between drafting the Peas card (which will add two new non-artichoke cards
    in total to your deck) or drafting the Onion card (which will simply remove one artichoke without
    adding any new cards). Which one gives you a better chance of winning on your next hand
    (assuming you shuffle all your cards and draw 5)? Justify your answer
    """
    import itertools
    total_hands = 0
    zero_artichokes = 0
    artichokes = set(["A1", "A2"])

    if 'A2' not in deck:
        artichokes = set(["A1"])
    
    for hand in itertools.combinations(deck, num_draw):
        total_hands += 1
        if not set(hand) & artichokes: #check if the hand has exactly zero
            zero_artichokes += 1
        
    probability = zero_artichokes / total_hands
    return probability, total_hands, zero_artichokes

def question4():
    print("\n========== Question 4 ==========")
    #option 1: peas card
    deck_peas = ["A1", "A2"] + ["N1", 'N2', 'N3', 'N4', 'N5', 'N6', 'N7']

    #option 2: onion card
    deck_onion = ["A1"] + ["N1", 'N2', 'N3', 'N4', 'N5']

    prob_peas, total_peas_hands, zero_peas = calculate_probability_zero_artichokes(deck_peas)
    print("Option 1: Drafting the Peas Card")
    print(f"Total hands: {total_peas_hands}")
    print(f"Hands with exactly zero artichokes: {zero_peas}")
    print(f"Probability of exactly zero artichokes: {prob_peas:.4%}\n")

    prob_onion, total_onion_hands, zero_onion = calculate_probability_zero_artichokes(deck_onion)
    print("Option 2: Drafting the Onion Card")
    print(f"Total hands: {total_onion_hands}")
    print(f"Hands with exactly zero artichokes: {zero_onion}")
    print(f"Probability of exactly zero artichokes: {prob_onion:.4%}\n")

    #compare probabilities
    if prob_peas > prob_onion:
        better_option = "Option 1: Drafting the Peas Card"
    elif prob_peas < prob_onion:
        better_option = "Option 2: Drafting the Onion Card"
    else:
        better_option = "Both options are equally effective."
    
    print(f"**Better Choice:** {better_option}")

question1()
question2()
question3()
question4()
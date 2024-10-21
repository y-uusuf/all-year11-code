import random as r


def initiate():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♥', '♦', '♣', '♠']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    r.shuffle(deck)
    return deck

def compare(x, y):
    ranks_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    rank1 = x['rank']
    rank2 = y['rank']

    if ranks_order.index(rank1) > ranks_order.index(rank2):
        return 1
    elif ranks_order.index(rank1) < ranks_order.index(rank2):
        return 2
    else:
        return 0

def play():
    deck = initiate()
    player1_hand = deck[:26]
    player2_hand = deck[26:]

    rounds_played = 0

    while player1_hand and player2_hand:
        rounds_played += 1
        print(f"\nRound {rounds_played}")

        card1 = player1_hand.pop(0)
        card2 = player2_hand.pop(0)

        print(f"Player 1 draws {card1['rank']} of {card1['suit']}")
        print(f"Player 2 draws {card2['rank']} of {card2['suit']}")

        winner = compare(card1, card2)

        if winner == 1:
            print("Player 1 wins this round!\n")
            player1_hand.extend([card1, card2])
        elif winner == 2:
            print("Player 2 wins this round!\n")
            player2_hand.extend([card1, card2])
        else:
            print("It's a tie! Let's commence war!..\n")
            player1_hand.extend([card1])
            player2_hand.extend([card2])

    if player1_hand:
        print("Player 1 wins the game!")
    else:
        print("Player 2 wins the game!")

play()

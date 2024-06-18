import random

# Card constraints
SUIT_TUPLE = ("Spades", "Hearts", "Clubs", "Diamond")
RANK_TUPLE = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")

NCARDS = 8

def get_card(deck_list_in):
    this_card = deck_list_in.pop()
    return this_card

def shuffle(deck_list_in):
    deck_list_out = deck_list_in.copy()
    random.shuffle(deck_list_out)
    return deck_list_out

# Main Code
print("Welcome to Higher or Lower")
print("You can choose whether the next card will be higher and lower than the current card")
print("If  you're right, you get 20 points, else you'll get -15")
print("You have 50 points to start with")
print()

# create a list that stores the details of each card as a dict
starting_deck_list = []
for suit in SUIT_TUPLE:
    for this_value, rank in enumerate(RANK_TUPLE):
        card_dict = {'rank': rank, 'suit':suit, 'value':this_value+1}
        starting_deck_list.append(card_dict)
        
score = 50

while True:
    print()
    game_deck_list = shuffle(starting_deck_list)
    current_card_dict = get_card(game_deck_list)
    current_card_rank = current_card_dict['rank']
    current_card_suit = current_card_dict['suit']
    current_card_value = current_card_dict['value']
    
    print(f"The starting card is {current_card_rank} and suit is {current_card_suit} ")
    print()
    
    for card_number in range(0, NCARDS):
        answer = input(f"Will the next card number of {current_card_rank}  and {current_card_suit} be higher or lower? (Enter h or l)")
        answer = answer.casefold() # force lowercase
        next_card_dict = get_card(game_deck_list)
        next_card_rank = next_card_dict['rank']
        next_card_suit = next_card_dict['suit']
        next_card_value = next_card_dict['value']
        print(f"the next card is, {next_card_rank} and of {next_card_suit}")
        
        
        
        if answer == 'h' and next_card_value > current_card_value:
            print("You're right. You got it")
            score += 20
        elif answer == 'l' and next_card_value < current_card_value:
            print("Yes, you got it right")
            score += 20
        
        else:
            print("Sorry, you got it wrong")
            score -= 15
            
        print(f"Your score is: {score}")
        print()
        current_card_rank = next_card_rank
        current_card_value = next_card_value
        current_card_suit = next_card_suit
        
    go_again = input("To play again press ENTER, or q to quit: ")
    if go_again == 'q':
        break
print("Ok bye")
import random

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suites = ['♥', '♠', '♣', '♦']
card_stack = []
desk = []
hand = []




def cards_defined():

    def random_card():
        random_card = random.choice(cards) + random.choice(suites)
        return random_card

    def duplicate_check(arg_list):
        for element in arg_list:
            if element == element:
                arg_list.remove(element)
                card_stack.append(random_card())

    for _ in range(7):
        card_stack.append(random_card())
        duplicate_check(card_stack)

    desk.extend(card_stack[0:5])
    hand.extend(card_stack[5:7])


def combination_check():
    





def cards_choose(call):
    if 'init_flop' in call:
        return card_stack[0:3]
    elif 'init_turn' in call:
        return card_stack[3]
    elif 'init_river' in call:
        return card_stack[4]
    elif 'give_hand' in call:
        return card_stack[5:7]



cards_defined()

print(cards_choose('init_flop'))
print(cards_choose('init_turn'))
print(cards_choose('init_river'))
print(cards_choose('give_hand'))
print(desk)
print(hand)



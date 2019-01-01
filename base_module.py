def start_position(role):
    role = int(role)
    positions = ["Dealer", "Small blind", "Big blind"]
    return positions[role]

def next_round(position):
    if position > 2:
        position = 0
    return start_position(position)


def dialog():
    print("Game started. Make your bet")
    bet = input(">")
    print("This was a preflop. Now flop")
    flop()
    print("Make your bet again")
    bet = input(">")
    print("Now turn")
    turn()
    print("Make your bet again")
    bet = input(">")
    print("Now river")
    river()
    print("Make your bet again")
    bet = input(">")
    print("You won")


def flop():
    pass
def turn():
    pass
def river():
    pass

def start():
    count = 0
    status = start_position(count)
    while True:
        print("Welcome to our poker desk")
        print(f"You are starting game as {status}")
        dialog()
        print("Do you wish to continue?")
        answer = input(">")
        if 'y' in answer:
            count += 1
            status = next_round(count)
            continue
        else:
            break

start()









#def change_status():
    #dealer, small_blind, big_blind = 0, 1, 2
        #if position == 0:
        #print("You're a dealer")
        #position += 1
        #print(position)
    #elif position == 1:
        #print("Small blind")
        #position += 1
        #print(position)
    #elif position == 2:
        #print("Big blind")
        #position = 0 
        #print(position)
























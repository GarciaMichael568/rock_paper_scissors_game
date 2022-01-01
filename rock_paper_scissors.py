import random 

def play():
    user = input("Input choice: 'r' for rock, 'p' for paper, 's' for scissors.\n")
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        return 'Tie buddy.'
    if is_win(user, computer):
        return 'WINNER WINNER CHICKEN DINNER!'
    
    return 'You Lost!'
def is_win(player, opponent):
    #return true if player wins
    # r > s, s > p, p > r
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
    
if __name__ == "__main__":
    print(play())
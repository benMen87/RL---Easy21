import card
import numpy as np

MAX_VAL = 21
MIN_VAL = 0 
DEALER_HIT_MAX = 17
EASY_21 = 21

HIT = 'hit'
MISS = 'miss'
actions = [HIT, MISS]

def step(dealer_firstcard, player_sum, action):
    dealer_sum = dealer_firstcard
    reward = 0

    if action == HIT:
        player_sum = hit(player_sum)
        if not inrange(player_sum):
            reward = -1
        if player_sum == EASY_21:
            reward = 1
    elif action == MISS:
        while dealer_sum in range(MIN_VAL, DEALER_HIT_MAX):
            dealer_sum += hit(dealer_sum)
        if not inrange(player_sum):
            reward = -1
        if dealer_sum > player_sum:
            reward = -1
        if player_sum > dealer_sum:
            reward = 1
    return dealer_firstcard, player_sum, action, reward

def inrange(sum):
    return p_sum in  range(MIN_VAL, MAX_VAL + 1)
        
def get_rand_action():
     return np.random.choice(len(actions), p=[1/2]*2)

def hit(curr_sum):
    val, color = card.draw_card()
    
    if color == card.BLACK:
        sum = sum + curr_sum
    elif color == card.RED:
        sum = sum - curr_sum
    else:
        raise ValueError("Undef color")
    return sum

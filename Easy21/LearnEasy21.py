import Easy21
from collections import namedtuple


N0 = 100
N = dict()
Q = dict()
S = namedtuple("easy21_state", ["player_sum", "dealer_sum"])

def creat_state(player_sum, dealer_sum):
    return S(player_sum=player_sum, dealer_sum=dealer_sum)

def update_N(state, action):
     


def monte_carlos_easy21():

    #value func
    v = 0

    
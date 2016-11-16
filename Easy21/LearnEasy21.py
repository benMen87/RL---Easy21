import Easy21
from collections import namedtuple


N0 = 100
N = dict()
Q = dict()
S = namedtuple("easy21_state", ["player_sum", "dealer_sum"])
SA = namedtuple("easy21_state_action", ["state", "action"])

def creat_state(player_sum, dealer_sum):
    return S(player_sum=player_sum, dealer_sum=dealer_sum)

def create_state_action_pair(state, action):
    return SA(state=state, action=action)

def update_N(state_action):
    N[state_action] = N.get(state_action, 0) + 1

def get_stateaction_N(state_action):
    return N.get(state_action, 0)

def update_Q(state_action, G):
    Q[state_action] = Q.get(state_action, 0) + 1/max(get_stateaction_N(state_action), 1) * (G - Q.get(state_action, 0))
    


def monte_carlos_easy21():

    #value func
    v = 0

    
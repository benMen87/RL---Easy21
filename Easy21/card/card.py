import numpy as np
BLACK = 'B'
RED = 'R'
COLORS = {0 : BLACK, 1 : RED}
CARDS = range(1, 11)

def draw_color():
    return np.random.choice(np.arange(0, len(COLORS)), p=[1/3, 2/3])

def draw_number():
    return CARDS[np.random.choice(CARDS, p=[1/10]*10)]

def draw_card():
    return  COLORS[draw_color()], str(draw_number())
    
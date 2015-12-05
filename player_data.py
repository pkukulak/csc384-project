from player import *
from itertools import product
import random

NUM_PLAYERS = 10

FIRST_NAMES = ["Randy", "Stephen", "Alex", "Targus",
               "Samuel", "Portland", "Justin", "Epcott",
               "Karter", "Joplin-Jones", "Madman"]

LAST_NAMES = ["Stormer", "Batplish", "Goldman-Sachs", "Sik",
              "Wu", "Wu-Jonestown", "Smee", "Urinaea",
              "Curry", "Bryant", "George"]

ALL_NAMES = list(product(FIRST_NAMES, LAST_NAMES))

def random_players():
    '''
    Return a PlayerPool of NUM_PLAYERS randomly-generated Player objects.
    '''
    names = random.sample(ALL_NAMES, NUM_PLAYERS)
    heights = [random.uniform(5.4, 6.8) for _ in range(NUM_PLAYERS)]
    weights = [random.randint(120, 250) for _ in range(NUM_PLAYERS)]
    ages = [random.randint(19,35) for _ in range(NUM_PLAYERS)]
    prices = [random.randint(10000,100000) for _ in range(NUM_PLAYERS)]
    gp = [random.uniform(15.0, 25.0) for _ in range(NUM_PLAYERS)]
    gs = [random.uniform(10.0, 15.0) for _ in range(NUM_PLAYERS)]
    three_p = [random.random() for _ in range(NUM_PLAYERS)]
    ppg = [random.uniform(25.0, 55.0) for _ in range(NUM_PLAYERS)]

    players = []
    for i in range(NUM_PLAYERS):
        name = names[i]
        height = heights[i]
        weight = weights[i]
        age = ages[i]
        price = prices[i]
        player_gp = gp[i]
        player_gs = gs[i]
        player_three_p = three_p[i]
        player_ppg = ppg[i]
        players += [Player(name, height, weight, age, price, player_gp,
                           player_gs, player_three_p, player_ppg)]

    return PlayerPool(players)

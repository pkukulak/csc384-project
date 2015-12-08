from player import *
from itertools import product
import random
from bball_csp import *

NUM_PLAYERS = 20

FIRST_NAMES = ["Randy", "Stephen", "Alex", "Targus",
               "Samuel", "Portland", "Justin", "Epcott",
               "Karter", "Joplin-Jones", "Madman", "Osama",
               "Spindler", "Spangler", "Shawn", "Sean"]

LAST_NAMES = ["Stormer", "Batplish", "Goldman-Sachs", "Sik",
              "Wu", "Wu-Jonestown", "Smee", "Urinaea",
              "Curry", "Bryant", "George", "Gleave Riemann",
              "Tonka", "Callabasus", "Iron", "Sturmgewehr"]

ALL_NAMES = list(product(FIRST_NAMES, LAST_NAMES))

def test_list():
    '''
    Return a PlayerPool of NUM_PLAYERS
    '''
    Players = []

    Players.append(Player("Lebron James", 6.4, 220, 31, 100000, 25, 20, .53, 30))
    Players.append(Player("Steph Curry", 6.0, 160, 25, 50500, 15, 5, .65, 22))
    Players.append(Player("Michael Jordan", 6.4, 240, 43, 75900, 25, 10, .67, 45))
    Players.append(Player("Fahiem Bacchus", 6.8, 260, 25, 100000, 25, 10, .80, 55))
    Players.append(Player("Kobe Bryant", 6.0, 200, 31, 40000, 20, 15, .64, 35))

    Players.append(Player("Jimmy Butler", 5,8, 160, 40, 20500, 15, 5, .42, 14))
    Players.append(Player("Russell Westbrook", 6.0, , 24, 30000, 25, 20, .47, 26))
    Players.append(Player("Jamal Crawford", 6.6, 220, 26, 33000, 10, 5, .35, 16))
    Players.append(Player("Larry Bird", 6.0, 180, 28, 45000, 15, 6, .58, 40))
    Players.append(Player("Shaquille O Neal", 6.8, 250, 45, 22000, 15, 3, .25, 36))
    
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

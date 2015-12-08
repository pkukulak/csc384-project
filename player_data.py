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

    Players.append(Player("Jimmy Butler", 5.8, 160, 40, 20500, 15, 5, .42, 14))
    Players.append(Player("Russell Westbrook", 6.0, 160, 24, 30000, 25, 20, .47, 26))
    Players.append(Player("Jamal Crawford", 6.6, 220, 26, 33000, 10, 5, .35, 16))
    Players.append(Player("Larry Bird", 6.0, 180, 28, 45000, 15, 6, .58, 40))
    Players.append(Player("Shaquille O Neal", 6.8, 250, 45, 22000, 15, 3, .25, 36))

    Players.append(Player("James Harden", 6.2, 180, 21, 62570, 15, 15, .53, 28))
    Players.append(Player("Carmelo Anthony", 5.6, 160, 31, 28078, 20, 5, .48, 34))
    Players.append(Player("Karl Malone", 6.3, 205, 40, 36500, 20, 5, .21, 14))
    Players.append(Player("Steve Nash", 6.2, 200, 30, 72780, 15, 10, .36, 20))
    Players.append(Player("Charles Barkley", 6.5, 220, 45, 68040, 22, 10, .85, 50))

    Players.append(Player("Bill Russell", 5.6, 155, 34, 27600, 15, 5, .36, 25))
    Players.append(Player("Hakeem Olajuwon", 6.0, 185, 34, 40800, 20, 15, .15, 10))
    Players.append(Player("Kevin Durant", 6.2, 180, 32, 60890, 20, 15, .60, 35))
    Players.append(Player("Allen Iverson", 5.6, 155, 35, 78900, 10, 5, .56, 40))
    Players.append(Player("Dirk Nowitzki", 6.4, 200, 32, 42040, 15, 7, .67, 32))

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
        name = names[i][0] + ' ' + names[i][1]
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

def print_info(players):

  s = ''
  for player in players.get_players():
    s += 'Name: ' + player.get_name() + ' Height: ' + str(player.get_height()) + \
          ' Weight: ' + str(player.get_weight()) + ' Age: ' + str(player.get_age()) \
          + ' Salary: ' + str(player.get_price()) + ' Games Played:' + str(player.get_games_played()) \
          + ' Games Started: ' + str(player.get_games_started()) + ' Three pointer: ' \
           + str(player.get_three_pointers()) + ' Points per Game: ' + str(player.get_points_per_game()) + '\n'
  print(s)

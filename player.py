class PlayerPool:
    '''
    A class representing a pool of potential
    basketball players.
    '''

    def __init__(self, players=[]):
        '''
        Initialize a PlayerPool object to contain players.
        '''
        self.players = players

class Player:
    '''
    A class representing a basketball player.
    '''

    def __init__(self, name='', height=0.0, weight=0, age=0,
            price=0, gp=0, gs=0, three_p=0.0, ppg=0.00):
        '''
        Initializes a Player object. Players are indentified
        by the following parameters:
            name - The name of the Player.
            height - The height of the Player.
            weight - The weight of the Player.
            age - The age of the Player.
            price - The price to acquire this Player
            gp - The gp (Games Played) by this Player.
            gs - The gs (Games Started) by this Player.
            three_p - The percentage of Three Pointers scored
                      by this Player.
            ppg - The ppg (Points Per Game) by this Player.
        '''
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.price = price
        self.gp = gp
        self.gs = gs
        self.three_p = three_p
        self.ppg = ppg

    def get_name(self):
        '''
        Return the name of this Player.
        '''
        return self.name

    def get_height(self):
        '''
        Return the height of this Player.
        '''
        return self.height

    def get_weight(self):
        '''
        Return the weight of this Player.
        '''
        return self.weight

    def get_age(self):
        '''
        Return the age of this Player.
        '''
        return self.age

    def get_price(self):
        '''
        Return the price required to acquired this Player.
        '''
        return self.price

    def get_games_played(self):
        '''
        Return the gp (Games Played) by this Player.
        '''
        return self.gp

    def get_games_started(self):
        '''
        Return the gs (Games Started) by this Player.
        '''
        return self.gs

    def get_three_pointers(self):
        '''
        Return the percentage of Three Pointers scored by this
        Player.
        '''
        return self.three_p

    def get_points_per_game(self):
        '''
        Return the average points scored by this Player.
        '''
        return self.ppg

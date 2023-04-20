"""Computed properties is simply to use the property decorator to create
properties that are computed on the go."""
import random

FOOTBALL_PLAYERS = ['Ronaldo', 'Casemiro', 'Bale', 'Vinicious', 'Benzema',
                    'Curtois', 'Modric', 'hazard', 'asensio', 'Jovic', 'Kross',
                    'Valverde', 'alaba', 'carvajal', 'nacho']

class RealMadridClub:

    def __init__(self):
        self.players = list(FOOTBALL_PLAYERS)

    # here everytime you call property best_player is very rare that you would
    # get the same twice in a raw
    @property
    def best_player(self):
        random_int = random.randint(0, len(FOOTBALL_PLAYERS) - 1)
        return self.players[random_int]


madrid_club = RealMadridClub()
print(f'a = {madrid_club.best_player}')
print(f'b = {madrid_club.best_player}')
print(f'c = {madrid_club.best_player}')

import random
from Player import Player

class Team:

    def __init__(self, id):
        self.id = id
        self.playerlist = self.generatePlayers()

    def generatePlayers(self):
        players = []
        for i in range(7):
            players.append(Player(random.randint(160, 190), random.randint(50, 100), 0))
        return players
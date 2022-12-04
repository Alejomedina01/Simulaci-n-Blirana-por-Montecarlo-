import random

from Team import Team


class Round:
    initialTryRanges = [0, 6, 11, 21, 33, 48, 63, 81, 100]
    points = [0, 200, 150, 100, 40, 50, 25, 20]

    def __init__(self):
        self.pointPerPlayer = []

    def playRoundPerTeam(self, team):
        result = []
        for player in team.playerlist:
            result.append(self.triesPerPlayer(self, player))
        return result

    def triesPerPlayer(self, player):
        self.calculateRangesPerBeers(self, player)
        self.calculateRangesPerIMC(self, player)
        print(self.initialTryRanges)
        result = []
        for i in range(6):
            pseudo = random.randint(0, 100)
            result.append(self.oneTryOnePlayer(self, pseudo, player))
        return result

    def oneTryOnePlayer(self, pseudo, player):
        result = 0
        for i in range(len(self.initialTryRanges)):
            if i < 8:
                if self.initialTryRanges[i] <= pseudo <= self.initialTryRanges[i + 1]:
                    result = self.points[i]
                    break
        return result

    def calculateRangesPerBeers(self, player):
        if 2 <= player.beersNumber <= 4:
            self.initialTryRanges = [0, 9, 13, 22, 33, 48, 63, 81, 100]
        elif 5 <= player.beersNumber <= 7:
            self.initialTryRanges = [0, 11, 14, 23, 33, 48, 63, 81, 100]
        else:
            self.initialTryRanges = [0, 12, 15, 23, 33, 48, 63, 81, 100]

    def calculateIMC(self, player):
        return player.weight / (player.heigth / 100) ** 2

    def calculateRangesPerIMC(self, player):
        if player.beersNumber > 5:
            imc = self.calculateIMC(self, player)
            if imc >= 28:
                self.initialTryRanges[1] -= 3
                self.initialTryRanges[2] += 1
                self.initialTryRanges[3] += 1
                self.initialTryRanges[4] += 1
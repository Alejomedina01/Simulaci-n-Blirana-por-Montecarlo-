import random


class Round:
    initialTryRanges = [0, 6, 24, 39, 51, 61, 71, 85, 100]
    points = [0, 200, 150, 100, 40, 50, 25, 20]

    def __init__(self):
        self.pointPerPlayer = []

    def playRoundPerTeam(self, team):
        result = []
        for player in team.playerlist:
            points = self.triesPerPlayer(self, player)
            player.finalPoints += sum(points)
            result.append(points)
        return result


    def triesPerPlayer(self, player):
        self.calculateRangesPerBeers(self, player)
        self.calculateRangesPerIMC(self, player)
        # print(self.initialTryRanges)
        result = []
        for i in range(6):
            pseudo = random.randint(0, 100)
            points = self.oneTryOnePlayer(self, pseudo, player)
            result.append(points)
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
        if 2 <= player.beersNumber <= 5:
            self.initialTryRanges = [0, 10, 22, 32, 43, 56, 69, 84, 100]
        elif 6 <= player.beersNumber <= 10:
            self.initialTryRanges = [0, 20, 23, 29, 37, 52, 63, 81, 100]
        elif player.beersNumber > 10:
            self.initialTryRanges = [0, 30, 32, 36, 44, 56, 66, 81, 100]

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
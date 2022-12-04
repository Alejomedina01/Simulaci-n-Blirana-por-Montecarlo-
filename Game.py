from Round import Round
import random


class Game:

    def __init__(self, teamsList):
        self.teamsList = teamsList
        self.worstTeam = 0
        self.resultTeams = []
        self.calculateBeersPlayersTeams()
        self.calculateWorstAndContinueTeams()

    def calculateBeersPlayersTeams(self):
        for i in self.teamsList:
            for j in range(7):
                i.playerlist[j].beersNumber += random.randint(0, 3)

    def sumPointsPerPlayer(self, listPointsPerPlayer):
        result = 0
        for i in listPointsPerPlayer:
            result += i
        return result

    def sumPointsTotalTeam(self, roundPerTeam):
        sumTotalTeam = 0
        for i in roundPerTeam:
            sumTotalTeam += self.sumPointsPerPlayer(i)
        # print("resultado equipo -", sumTotalTeam)
        return sumTotalTeam

    def playRoundTeamsList(self):
        resultsRoundsPerTeams = []
        for i in range(5):
            round = Round.playRoundPerTeam(Round, self.teamsList[i])
            print("rondaaas - ", round)
            resultsRoundsPerTeams.append([i, self.sumPointsTotalTeam(round)])
            print("Total ronda equipo - ", self.teamsList[i].id ," - ", self.sumPointsTotalTeam(round))
        return resultsRoundsPerTeams

    def calculateWorstAndContinueTeams(self):
        list = self.playRoundTeamsList()
        indexWorstTeam = 0
        worstAux = list[0][1]
        for i in list:
            if i[1] <= worstAux:
                worstAux = i[1]
                indexWorstTeam = i[0]
        self.worstTeam = self.teamsList[indexWorstTeam]
        for i in range(5):
            if i != indexWorstTeam:
                self.resultTeams.append(self.teamsList[i])
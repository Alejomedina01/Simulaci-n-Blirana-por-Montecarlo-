from Game import Game
from Team import Team


class Simulation:


    def __init__(self, allTeams):
        self.teamsList = allTeams
        self.listAux = self.teamsList
        self.subs = []
        self.eliminados = []
        self.continuan = []
        self.playSimulation(self)

    def playGame(self, teams):
        game = Game(teams)
        self.deleteLoserTeam(self, game)
        self.nextTeams(self, game)

    def deleteLoserTeam(self, game):
        for i in self.teamsList:
            if i.id == game.worstTeam.id:
                print(game.worstTeam)
                print("ELIMINADO -> ", i.id)
                self.eliminados.append(i)

    def nextTeams(self, game):
        self.continuan.extend(game.resultTeams)

    def calculateSubLists(self):
        i = 0
        j = 5
        while(j <= len(self.teamsList)):
            self.subs.append(self.teamsList[i:j])
            print(self.teamsList[i:j])
            i = j
            j += 5

    def playSimulation(self):
        self.calculateSubLists(self)
        for i in self.subs:
            self.playGame(self, i)



allTeamsList = []
for i in range(100):
    team = Team(i)
    allTeamsList.append(team)

print("Iniciales")
for i in allTeamsList:
    print(i.id)

simulation = Simulation(allTeamsList)
# print(len(continuan))
# print("final")
# for i in continuan:
#     print(i.id)
# #
# for i in eliminados:
#     print("eliminado ", i.id)




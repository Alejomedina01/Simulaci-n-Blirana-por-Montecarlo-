from Game import Game
from Team import Team
from matplotlib import pyplot as plt


class Simulation:

    def __init__(self, teamsLists, id):
        self.id = id
        self.teamsList = teamsLists
        self.subs = []
        self.eliminados = []
        self.continuan = []
        self.playSimulation()

    def playGame(self, teams):
        game = Game(teams)
        self.deleteLoserTeam(game)
        self.nextTeams(game)

    def deleteLoserTeam(self, game):
        for i in self.teamsList:
            if i.id == game.worstTeam.id:
                print("ELIMINADO -> ", i.id)
                self.eliminados.append(i)

    def nextTeams(self, game):
        self.continuan.extend(game.resultTeams)

    def calculateSubLists(self):
        self.subs.clear()
        aux = self.auxFunction(len(self.teamsList))
        i = 0
        j = aux
        while(j <= len(self.teamsList)):
            self.subs.append(self.teamsList[i:j])
            print(self.teamsList[i:j])
            i = j
            j += aux

    def auxFunction(self, number):
        number = number
        aux = 5
        while (number % aux) != 0:
            aux -= 1
        return aux

    def playSimulation(self):
        self.calculateSubLists()
        self.continuan.clear()
        for i in self.subs:
            self.playGame(i)

    def printPlots(self):
        beersList = []
        pointsList = []
        for i in self.continuan:
            for j in i.playerlist:
                # print(j.id, "cervezas: ", j.beersNumber, "puntaje: ", j.finalPoints)
                beersList.append(j.beersNumber)
                pointsList.append(j.finalPoints)
        plt.plot(beersList, pointsList, "ro")
        plt.title("Grafica Cervezas vs Puntos x cada jugador (numero: "+ str(self.id)+ ")")
        plt.show()

#SIMULACIÓN

#Generación de los equipos
auxList = []
for i in range(100):
    team = Team(i)
    auxList.append(team)

aux = auxList

#Creación de la simulacion hasta quedar 3 equipos finalistas
simulations = []
id = 1
while(len(aux) >= 4):
    simu = Simulation(aux, id)
    id += 1
    print("finalistas ", len(simu.continuan))
    simu.printPlots()
    aux = simu.continuan


#Grafica de los 3 equipos finalistas
beersNumber = []
finalPoints = []
for i in aux:
    for j in i.playerlist:
        print(j.id, "   ----Cervezas:  ", j.beersNumber, "     ----Puntos: ", j.finalPoints)
        beersNumber.append(j.beersNumber)
        finalPoints.append(j.finalPoints)

plt.title("Jugadores de los 3 mejores equipos")
plt.plot(beersNumber, finalPoints, "ro")
plt.show()

#Equipo Ganador
while(len(aux) >= 2):
    simu = Simulation(aux, id)
    id += 1
    print("finalistas ", len(simu.continuan))
    simu.printPlots()
    aux = simu.continuan

print("Equipo Ganador: ", aux[0].id)
for x in aux[0].playerlist:
    print("id: ", x.id, "Cervezas: ", x.beersNumber, "Puntaje: ", x.finalPoints)

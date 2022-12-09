from Game import Game
from Team import Team

teamsList = []
subs = []
eliminados = []
continuan = []


def playGame(teams):
    game = Game(teams)
    deleteLoserTeam(game)
    nextTeams(game)

def deleteLoserTeam(game):
    for i in teamsList:
        if i.id == game.worstTeam.id:
            print(game.worstTeam)
            print("ELIMINADO -> ", i.id)
            eliminados.append(i)

def nextTeams(game):
    continuan.extend(game.resultTeams)

def calculateSubLists():
    subs.clear()
    aux = auxFunction(len(teamsList))
    i = 0
    j = aux
    while(j <= len(teamsList)):
        subs.append(teamsList[i:j])
        print(teamsList[i:j])
        i = j
        j += aux

def auxFunction(number):
    number = number
    aux = 5
    while (number % aux) != 0:
        aux -= 1
    return aux

def playSimulation():
    calculateSubLists()
    continuan.clear()
    for i in subs:
        playGame(i)



#SIMULACIÓN

auxList = []
for i in range(100):
    team = Team(i)
    auxList.append(team)

teamsList = auxList

print("Iniciales")
for i in teamsList:
    print(i.id)

playSimulation()

print(len(continuan))
print("final")
for i in continuan:
    print("continua ", i.id)

for i in eliminados:
    print("eliminado ", i.id)

teamsList.clear()
teamsList = continuan

print("Iniciales")
for i in teamsList:
    print(i.id)

playSimulation()

print(len(continuan))
print("final")
for i in continuan:
    print("continua ", i.id)

for i in eliminados:
    print("eliminado ", i.id)

teamsList.clear()
teamsList = continuan

print("conti ", teamsList)







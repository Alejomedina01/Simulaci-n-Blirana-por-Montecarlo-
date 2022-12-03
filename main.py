from Game import Game
import random
from Team import Team


teamsList = []
for i in range(5):
    team = Team(i)
    teamsList.append(team)


generalList = []

game = Game(teamsList)
todosEquipos = game.teamsList
peorEquipo = game.worstTeam
continuanEquipos = game.resultTeams


for i in todosEquipos:
    print("Equipo ", i.id)

for j in continuanEquipos:
    print("Continua ", j.id)
    for k in range(7):
        print(j.id, " - ", i.playerlist[k].beersNumber)

print("Peor ", peorEquipo.id)

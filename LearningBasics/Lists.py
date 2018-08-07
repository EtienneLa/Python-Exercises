players = [29, 50, 66, 71, 87]

for i in players:
    print(i)

print(players[2])
players[2] = 68
print(players[2])

players.append(120)
print(players)

players_sliced = players[:2]
print(players_sliced)
print(players[:2])

players[:3] = [0, 0, 0]
print(players)

players[:2] = []
print(players)

players[:] = []
print(players)



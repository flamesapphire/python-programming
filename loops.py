#loops

players=[1,2,2,4,5,6,7,8,9,0,1,12,12,1,14]

for p in players:
	if p%5 == 0:
		print(players[p])
	p += 5

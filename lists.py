#lists

players=[1,2,2,4,5,6]


players.append(10)
players[1:-3]=[10,10]
y = players
print y

if players[1]is players[2]:
 print("yes")

elif players[3]is players[4]:
  print ("no")

else :
 print ("!")

from random import choice

s = []

print("Enter The name 6 of player's you want to add :")

player1 = input("Enter the name of player you want to add + \r")
player2 = input("Enter the name of player you want to add +\r")
player3 = input("Enter the name of player you want to add + \r")
player4 = input("Enter the name of player you want to add + \r")
player5 = input("Enter the name of player you want to add + \r")
player6 = input("Enter the name of player you want to add + \r")

t1 = input("\n""enter the name of Team-1 : ")
t2 = input("enter the name of Team-2 : ")

s.append(player1)
s.append(player2)
s.append(player3)
s.append(player4)
s.append(player5)
s.append(player6)


team1 = []
team2 = []

p1 = choice(s)
team1.append(p1)
s.remove(p1)

p2 = choice(s)
team1.append(p2)
s.remove(p2)

p3 = choice(s)
team1.append(p3)
s.remove(p3)

p4 = choice(s)
team2.append(p4)
s.remove(p4)

p5 = choice(s)
team2.append(p5)
s.remove(p5)

p6 = choice(s)
team2.append(p6)
s.remove(p6)


print("\n"f"Team - {t1}")
for i in team1:
    print("\t",end="")
    print(i)


print("\n"f"Team - {t2}")
for i in team2:
    print("\t",end = "")
    print(i)


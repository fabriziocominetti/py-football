from random import seed
from random import randint
team1 = (input("Please enter the first team: "))
team2 = (input("Please enter the second team: "))
team3 = (input("Please enter the third team: "))
team4 = (input("Please enter the fourth team: "))
for i in range(5):
    score1 = randint(0,5)
for i in range(5):
    score2 = randint(0,5)
for i in range(5):
    score3 = randint(0,5)
for i in range(5):
    score4 = randint(0,5)
points1 = 0
points2 = 0
points3 = 0
points4 = 0
#matches
print("1st round")
print("Final Score: "+team1.upper()+" "+str(score1)+" : "+team2.upper()+" "+str(score2))
if str(score1) > str(score2):
    points1 += 3
elif str(score1) == str(score2):
    points1 += 1
    points2 += 1
else:
    points2 += 3
print("Final Score: "+team3.upper()+" "+str(score3)+" : "+team4.upper()+" "+str(score4))
if str(score3) > str(score4):
    points3 += 3
elif str(score3) == str(score4):
    points3 += 1
    points4 += 1
else:
    points4 += 3
print("2nd round")
print("Final Score: "+team1.upper()+" "+str(score1)+" : "+team3.upper()+" "+str(score3))
if str(score1) > str(score3):
    points1 += 3
elif str(score1) == str(score3):
    points1 += 1
    points3 += 1
else:
    points3 += 3
print("Final Score: "+team4.upper()+" "+str(score4)+" : "+team2.upper()+" "+str(score2))
if str(score4) > str(score2):
    points4 += 3
elif str(score4) == str(score2):
    points4 += 1
    points2 += 1
else:
    points2 += 3
print("3rd round")
print("Final Score: "+team1.upper()+" "+str(score1)+" : "+team4.upper()+" "+str(score4))
if str(score1) > str(score4):
    points1 += 3
elif str(score1) == str(score4):
    points1 += 1
    points4 += 1
else:
    points4 += 3
print("Final Score: "+team2.upper()+" "+str(score2)+" : "+team3.upper()+" "+str(score3))
if str(score2) > str(score3):
    points2 += 3
elif str(score2) == str(score3):
    points2 += 1
    points3 += 1
else:
    points3 += 3
#league table
print("| "+team1.upper()+" | "+str(points1))
print("| "+team2.upper()+" | "+str(points2))
print("| "+team3.upper()+" | "+str(points3))
print("| "+team4.upper()+" | "+str(points4))
#winner
if points1 > points2 and points1 > points3 and points1 > points4:
    print("The winner is: "+team1.upper())
if points2 > points1 and points2 > points3 and points2 > points4:
    print("The winner is: "+team2.upper())
if points3 > points1 and points3 > points2 and points3 > points4:
    print("The winner is: "+team3.upper())
if points4 > points1 and points4 > points2 and points4 > points3:
    print("The winner is: "+team4.upper())

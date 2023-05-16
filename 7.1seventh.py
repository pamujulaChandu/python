import random
# function to caluculate the addition of 2 dice numbers
def roll_dice():
  
        total_dice=random.randint(1,6)+random.randint(1,6)
        return total_dice
#getting players name to differentiate 
player1=input("player1 name :")
player2=input("player2 name : ")
total1=0
total2=0
#callling the function to get the dice number total
for i in range(0,3):
    roll1=roll_dice()
    roll2=roll_dice()
#printing the players rolled numbers
    print(player1 , "rolled", roll1)
    print(player2 , "rolled", roll2)
    total1= total1 + roll1
    total2=total2+roll2
print(total1 ,"of", player1 , "rolled")
print(total2 ,"of", player2 , "rolled")

#codition to know who own 

if(total1>total2):
    print(player1,"wins")
elif(total1<total2):
    print(player2,"wins")
else:
    print("TIE")

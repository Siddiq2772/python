import random

dict = {"snake":-1,"water":0,"gun":1}

comp = random.choice([-1,0,1])
player = dict[input("Enter your Choice: ")]

print(f"your choice: {player}")
print(f"computer choice: {comp}")
if(comp==player):
    print("draw")
elif(comp<player):
    print("you win")
elif(player<comp):
    print("you lose")

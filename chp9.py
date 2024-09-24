# f= open("peom.txt")

# print(f.read().__contains__("twinkle"))

# f.close()
import random
def game():
    f=open("score","w")
    s=f.read()
    score = random.randint(1,64)
    if(s!=""):
        s=int(f)

    print(f"your score is {score}")
    if(score>s):
        f.write(str(score))

    return score

game()
    
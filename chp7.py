'''a = int(input("enter number:"))
for i in range(1,11):
    print(a,"*",i,"=",a*i)'''


'''list = ["aname","sname","sname","name"]

for l in list:
    if (l[0]=='s'):
        print(l)'''



'''a = int(input("enter number:"))
i=1
while(i<=10):
    print(a,"*",i,"=",a*i)
    i+=1
'''
n = int(input("enter number"))
for i in range(n):
    if(i ==0 or i == n-1):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print()



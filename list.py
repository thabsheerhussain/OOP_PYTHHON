from random import randint
name=[]
n=int(input("enter the no"))
for i in range(0,n):
    item=input('enter the names')
    name.append(item)

a=randint(1,n)
print(name[a])

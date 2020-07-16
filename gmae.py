n='0'
while(n != 'no' or n==1):
    from random import randint
    colour=['r','b','g','w','o']
    c=input("enter a letter 'r','b','g','w','o'")
    a=randint(1,6)
    if(c == colour[a]):
        print("true")
    else:
        print("false")
    n=input("press no to stop and countinue to 1")

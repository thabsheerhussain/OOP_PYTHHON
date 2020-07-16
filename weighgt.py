weight=int(input("ENTER WEIGHT in kg"))
height=int(input("ENTER height"))
bmi=weight/(height*height)
if (bmi<=18.5):
    print("underweight")
elif (bmi>=18.5 or bmi<=24.9):
    print("normalweight")
elif (bmi>=24.9 or bmi<=24.9):
    print("overweight")
else :
    print("obesity")

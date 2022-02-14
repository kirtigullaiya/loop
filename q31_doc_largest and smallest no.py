i=1
num=int(input("please enter number:"))
num1=int(input("please enter number:"))
while i<=3:
    # num=int(input("please enter number:"))
    # num1=int(input("please enter number:"))
    if num<num1:
        print(num1,"is greater")
    elif num1<num:
        print(num,"is greater")
    else:
        print("both are equal")
i+=1



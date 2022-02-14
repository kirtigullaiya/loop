i=1
while i<=5:
    num=int(input("please enter the number:"))
    i+=1
    if num==5:
        print("congo, you guessed it correctly.")
        break
    elif num<5 :
        print("keep try this is smaller.")
    else:
        print("keep try this is greater.") 
                          
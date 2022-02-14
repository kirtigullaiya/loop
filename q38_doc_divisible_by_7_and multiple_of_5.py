# between 1500 and 2700(both included) those numbers which are divisible by 7 and multiple of 5.

i=1500
while i<=2700:
    i+=1
    if i%7==0 and i%5==0:
        print("yes, this is divisible by 7 and multiple of 5=",i)

    
#  perfect number.
number=int(input("please enter number:"))
i=1
sum=0
while i<number:
    if number%i==0:
        print(i)
        sum+=i
    i+=1
if sum==number:
    print("yes")
else:
    print("no")


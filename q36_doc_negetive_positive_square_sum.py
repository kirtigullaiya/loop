i=1
sum=0
sum1=0
num=int(input("please enter number:"))
while i<=num:
    k=i**2
    if i%2==0:
        sum=sum+i**2
        print(i)
        print(sum)
    else:
        sum1=sum1+(i**2)
        print(sum1)
    i=i+1
print("final sum=",sum+1-sum1)
i=1
sum=0
num=int(input("please enter number:"))
while i<=num:
    k=i**3
    # sum=sum+k
    i+=1
    sum=sum+k
    total=sum
    print("cubes:",k,"sum:",sum)
print("total is:",total)
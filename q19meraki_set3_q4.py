# sum of those numbers between 30 to 420 multiples of 8

i=30
sum=0
while i<=420:
    sum=sum+i
    if i%8==0:
        print(i)
    i+=1
print("total sum=",sum)
       
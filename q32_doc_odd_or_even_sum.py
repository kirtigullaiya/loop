i=100
sum=0
sum1=0
count=0
count1=0
while i<=500:
    if i%2==0:
        sum=sum+i
        count+=1
        # i+=1
        avg=sum/count
    # i+=1
# print(sum)
    else:
        sum1=sum1+i
        count1+=1
        avg1=sum1/count1
    i+=1
    # print(i)
print("sum of even numbers are:",sum,"\n","sum of odd numbers are :",sum1)
print(avg)
print(avg1)


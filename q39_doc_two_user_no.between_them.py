# take two user inputs and between them we have to take even numbers and sum up all of them.
sum=0
num=int(input("please enter the number:"))
num1=int(input("please enter the number:"))
while num<=num1:
    num+=1
    if num%2==0:
        sum=sum+num
        total=sum
        # print(num)
        # print(sum)
        print(num)
print("total is =",total)
i=0
num=int(input("please enter name:"))
while num>0:
    i=(i*10)+num%10
    num=num//10
print(i)

i=1
num=int(input("please enter number:"))
while i<=num:
    digit1=num//100%10
    digit2=num//10%10
    digit3=num%10
    sum=digit1+digit2+digit3
    i+=1
if num%sum==0:
    print(sum,"yes this is harsad number.")
else:
    print(sum,"1not a harshad number.")
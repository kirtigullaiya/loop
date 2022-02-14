i=0
num=int(input("please enter number:"))
temp=num
while 0<num:
    i=(i*10)+num%10
    num=num//10
print(i)
if i==temp:
    print("yes this is palinedrome number.")
else:
    print("no this is not a palindrome number.")
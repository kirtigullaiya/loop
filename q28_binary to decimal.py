# i=1
# k=0
# binary=int(input("enter binary number:"))
# while binary!=0:
#     rem=binary%10
#     k=k+(rem*i)
#     i=i*2
#     binary=int(binary/10)
# print(k)
# they both are same, but the difference is int and float.101
#  

i=1
k=0
num=int(input("please enter number:"))
while num>0:
    rem=num%10
    k=k+(rem*i)
    i=i*2
    num=num//10
print(k)
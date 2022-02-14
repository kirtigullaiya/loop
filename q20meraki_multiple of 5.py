# average of 11 people is the multiple of 5 or not

i=1
total=0
avg=total/11
while i<=11:
    num=int(input("please enter the number:"))
    total=total+num  
    i+=1
print(total)
avg=total/11
if avg%5==0:
    print(avg,"is divisible.")
else:
    print("not divisible")

    
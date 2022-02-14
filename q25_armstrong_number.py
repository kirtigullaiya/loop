i=1
num=int(input("please enter number:"))
while i<=num:                                                                              
    cube=(num//100%10)**3
    cube1=(num//10%10)**3
    cube2=(num%10)**3
    # cube=cube**3
    # cube1=cube1**3
    # cube2=cube2**3
    # i=i+1
    sum=cube+cube1+cube2
    i=i+1
if num==sum:
    print(sum,"yes it is an armstrong number.")
else:
    print(sum,"not an armstrong number.") 


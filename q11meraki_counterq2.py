# divisible by 3 print(nav) and by 7 print(gurukul) and by both print(navgurukul)
i=1
while i<=100:
    if i%3==0 and i%7==0:
        print("navgurukul")
    elif i%7==0:
        print("gurukul")
    elif i%3==0:
        print("nav")
    else:
        print(i)
    i+=1        
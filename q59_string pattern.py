string=input("please enter string:")
i=0
while i<len(string):
   j=0
   while j<=i:
      print(string[j],end=" ")
      j+=1
   print()
   i+=1

   k=1
   while k<=len(string)-1:
      print(" ",end="")
      k+=1
   j=0
   while j<=i:
      print(string[j],end="")
      j+=1
   print()
   i+=1



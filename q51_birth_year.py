i=1 
num=int(input("please enter number:"))
while i<=num:
    birth_year=int(input("plaese enter birth year:"))
    current_year=int(input("please enter current year:"))
    # i+=1
    if current_year>birth_year:
        print(current_year-birth_year)
    i+=1
    
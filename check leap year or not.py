year=int(input("enter the year to be checked"))
if year%4==0 and year%100!=0 or year%400==0:
    print("the given year is leap year:")
else:
    print("the given year is not leap year:")

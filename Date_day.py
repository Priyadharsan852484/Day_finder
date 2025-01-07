f=input("Enter First day in month : ")
n=int(input("Date to find day : "))
day=["SUN","MON","TUE","WED","THU","FRI","SAT"]

i=day.index(f)
d=day[i::]+day[0:i+1]
td=n%7
print(d[td-1])

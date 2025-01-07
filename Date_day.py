f=input()
n=int(input())
day=["SUN","MON","TUE","WED","THU","FRI","SAT"]

i=day.index(f)
d=day[i::]+day[0:i+1]
td=n%7
print(d,d[td-1])
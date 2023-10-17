n=int(input())
if(n%400==0) or (n%4==0 and n%100!=0):
     print("leaf year")
else:
     print("not a leaf year")
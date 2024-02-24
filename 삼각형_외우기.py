a=int(input())
b=int(input())
c=int(input())

if a==60 and b==60 and c==60 and a+b+c:
    print("Equilateral")
elif (a==b or b==c or c==a) and a+b+c==180:
    print("Isosceles")
elif a+b+c==180:
    print("Scalene")
else:
    print("Error")
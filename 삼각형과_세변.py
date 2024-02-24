while(1):
    a, b, c=map(int, input().split())
    if a==b and b==c and c==a:
        print("Equilateral")
    elif a==b or b==c or c==a:
        print("Isosceles")
    else:
        print("Scalene")
    if (a>=b+c) or(b>=a+c) or (c>=a+b):
        print("Invalid")
    if a==0 and b==0 and c==0:
        break
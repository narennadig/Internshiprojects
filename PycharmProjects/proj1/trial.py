term = 30
start_rate = 3
final_rate = 18
amount = 350000

for i in range(3,18):

    n=30*12
    p=i/100
    r=p/12
    d=((1 + r)**(n) - 1)/(r * (1 + r)**n)
    print(i+"  "+d)



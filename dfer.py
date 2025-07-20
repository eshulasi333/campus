triangle=[]
pentaganol=[]
hexagonal=[]
i=1
po=0
s=0
while True:
    if po==1:
        print(s)
        break
    a=i*(i+1)/2
    b=i*(3*i-1)/2
    c=i*(2*i-1)
    triangle.append(a)
    pentaganol.append(b)
    hexagonal.append(c)
    for y in triangle:
        if y in pentaganol and y in hexagonal:
            po+=1
            s=y
print(s)
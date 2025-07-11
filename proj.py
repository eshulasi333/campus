first=list(map(int,input().split()))
z=[]
for t in range(first[0]):
    d=list(map(int,input().split()))
    z.append(d)
second=list(map(int,input().split()))
f=[]
for p in range(second[0]):
    d=list(map(int,input().split()))
    f.append(d)
if len(z[0])!=len(f):
    print("matrices can't multipy")
    exit()
b=[]
for x in range(len(z)):
    p=[]
    for y in range(len(f[0])):
        c=0
        for a in range(len(z[0])):
            c+=z[x][a]*f[a][y]
        p.append(c)
    b.append(p)
for j in b:
    print(j)
size=list(map(int,input("enter row and coloumn ").split()))
row=size[0]
coloumn=size[1]
mine=0
print("enter numbers ")
for w in range(row):
    ty=list(map(int,input().split()))
    if len(ty)!=coloumn:
        print("invalid grid")
    er=max(ty)
    if mine<er:
        mine=er
print(mine)
    
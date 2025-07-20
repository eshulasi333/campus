def prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for x in range(3,int(n**(1/2))+1,2):
        if n%x==0:
            return False
    return True
pri=[]
se=[]
i=3

for x in range(3,9000,2):
    if prime(x):
        pri.append(x)
        
for y in range(len(pri)):
    for x in range(y+1,len(pri)):
        ab,ba=int(str(pri[y])+str(pri[x])),int(str(pri[x])+str(pri[y]))
        if not(prime(ab) and prime(ba)):
            continue
        for a in range(x+1,len(pri)):  
            bc,cb=int(str(pri[a])+str(pri[x])),int(str(pri[x])+str(pri[a]))
            cd,dc=int(str(pri[a])+str(pri[y])),int(str(pri[y])+str(pri[a]))
            if not( prime(bc) and prime(cd) and prime(cb) and (dc)):
                continue
            for b in range(a+1,len(pri)):
                dc,cd=int(str(pri[b])+str(pri[x])),int(str(pri[x])+str(pri[b]))
                ed,de=int(str(pri[b])+str(pri[y])),int(str(pri[y])+str(pri[b]))
                fd,df=int(str(pri[b])+str(pri[a])),int(str(pri[a])+str(pri[b]))
                if not(prime(dc) and prime(cd) and prime(ed) and prime(de) and prime(fd) and prime(df)):
                    continue
                for c in range(a+1,len(pri)):
                    hj,jh=int(str(pri[c])+str(pri[x])),int(str(pri[x])+str(pri[c]))
                    kl,lk=int(str(pri[c])+str(pri[y])),int(str(pri[y])+str(pri[c]))
                    lm,ml=int(str(pri[c])+str(pri[a])),int(str(pri[a])+str(pri[c]))
                    nm,mn=int(str(pri[b])+str(pri[c])),int(str(pri[c])+str(pri[b]))
                    if prime(hj) and prime(jh) and prime(kl) and prime(lk) and prime(lm) and prime(ml) and prime(mn) and prime(nm):
                        se.append((pri[y],pri[x],pri[a],pri[b],pri[c]))

su=sum(se[0])
ind=0
for i in se:
    for y in i:
        se=sum(i)
        if su>se:
            su=se
            ind=i
print(s[0],print(ind))
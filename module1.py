f=open('Perepis.txt')
a=0
q=int(input())
w=int(input())
for i in f:
    l=i.split()
    s=l[3]
    k=s.split('.')
    if(int(k[2])<1978):
        a=a+1
        print(l[0])
print(a)
f.close()
f=open('Perepis.txt')
for i in f:
    l=i.split()
    s=l[3]
    k=s.split('.')
    if(q<int(k[2])<w):
        print(l)
f.close()
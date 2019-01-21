f=open('mat_dv.txt')
max1=0
max2=0
max3=0
max4=0
m=0
for i in f:
    l=i.split(' ')
    v=int(l[2])
    q=int(l[3])
    w=int(l[4])
    m=q+w
    if((v==8)and(m>max1)):
        max1=m
        imya1=l[0]
        famil1=l[1]
    if((v==9)and(m>max2)):
        max2=m
        imya2=l[0]
        famil2=l[1]
    if((v==10)and(m>max3)):
        max3=m
        imya3=l[0]
        famil3=l[1]
    if((v==11)and(m>max4)):
        max4=m
        imya4=l[0]
        famil4=l[1]
print('8 класс',' ',imya1,' ',famil1,' ',max1)
print('9 класс',' ',imya2,' ',famil2,' ',max2)
print('10 класс',' ',imya3,' ',famil3,' ',max3)
print('11 класс',' ',imya4,' ',famil4,' ',max4)
f.close()
f=open('mat_dv.txt')
max1=0
max2=0
max3=0
max4=0
maxg1=0
maxg2=0
maxg3=0
maxg4=0
for i in f:
    l=i.split(' ')
    v=int(l[2])
    q=int(l[3])
    w=int(l[4])
    if((v==8)and(q>max1)and(w>maxg1)):
        max1=q
        maxg1=w
        imya1=l[0]
        famil1=l[1]
    if((v==9)and(q>max2)and(w>maxg2)):
        max2=q
        maxg2=w
        imya2=l[0]
        famil2=l[1]
    if((v==10)and(q>max3)and(w>maxg3)):
        max3=q
        maxg3=w
        imya3=l[0]
        famil3=l[1]
    if((v==11)and(q>max4)and(w>maxg4)):
        max4=q
        maxg4=w
        imya4=l[0]
        famil4=l[1]
print()
print('8 класс',' ',imya1,' ',famil1,' ','алгебра',' ',max1,'геометрия',' ',maxg1)
print('9 класс',' ',imya2,' ',famil2,' ','алгебра',' ',max2,'геометрия',' ',maxg2)
print('10 класс',' ',imya3,' ',famil3,' ','алгебра',' ',max3,'геометрия',' ',maxg3)
print('11 класс',' ',imya4,' ',famil4,' ','алгебра',' ',max4,'геометрия',' ',maxg4)
f.close()
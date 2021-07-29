def mxm(l):
    z=l[0][1]
    for p,q in l:
        if q>=z:
            z=q
    temp = []
    for r,s in l:
        if s==z:
            temp.append(r)
    return(f'{temp} occured maximum time, value =  {z}')




a = input('enter words or a line saperated by space: ')
a= a.lower()
# print(a)
a = a.split(' ')

emp = []
l=[]
for i in a:
    if i not in emp:
        x=a.count(i)
        emp.append(i)
        l.append([i,x])
        
print(mxm(l))

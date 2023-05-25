with open ("en-ru.txt","r+") as file:
    lr=[]
    le=[]
    for i in file:
        i=i.split('-')
        s=i[-1]
        s=s.replace('\n','')
        lr.append(s)
lr.sort()
r=len(le)
d={}
le2=[]
with open ("en-ru.txt","r+") as file3:
    for i in file3:
        i=i.replace('\n',"")
        ir=i.split('-')
        iru=ir[-1]
        d.update({iru:i})
del lr[0]
print(lr)
for i in lr:
    s2=d.get(i)
    s2=s2.split('-')
    le2.append(s2[0])
r=6
with open ("ru-en.txt","r+") as file2:
    for i in range(r):
        file2.write(str(lr[i]) + '-' + str(le2[i]) +'\n')

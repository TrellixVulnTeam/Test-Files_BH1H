'''
Bubble sort
l=eval(input())
for i in range(len(l)):
    for j in range(0,len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)            
'''
#Obvious sort
l=eval(input())
x=[]
while len(l)>0:
    min=l[0]
    for i in range(0,len(l)):
        if l[i]<min:
            min=l[i]
    l.remove(min)
    x.append(min)

print(x)    

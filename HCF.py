def HCF(a,b):
    if b==0:
        return a
    else:
        return HCF(b, a%b)
print(HCF(10213,312))    

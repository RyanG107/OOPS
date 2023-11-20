def maxnum(l):
    mx=l[0];
    for i in range(0,len(l)):
        if l[i]>mx:
            mx=l[i];
    return mx;

a=maxnum(l);
print(a);
    

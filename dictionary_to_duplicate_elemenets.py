a=list(map(str,input('Enter the keyword : ').split()))
b=list(map(str,input('Enter the corresponding values : ').split()))
out=dict(zip(a,b))
#print(out)
lst=[]
dct1={}
for i,j in out.items():
   if j not in lst:
       lst.append(j)
       dct1[i]=j
print(dct1)



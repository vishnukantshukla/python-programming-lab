def prime_numbber_or_not(x):
    for i in range(2,x):
        if x%i==0:
            return False
    else:
        return True

lst=[1,2,3,4,5,6,7,8,9,10]
lst1=[]
for i in lst:
    if prime_numbber_or_not(i):
        lst1.append(i)
print(lst1)
    
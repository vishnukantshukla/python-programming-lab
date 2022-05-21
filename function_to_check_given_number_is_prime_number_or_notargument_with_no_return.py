def info(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count=count+1
    if count==2:
        return 'Prime number '
    else:
        return 'Not Prime number'
a=int(input())
out=info(a)
print(out)
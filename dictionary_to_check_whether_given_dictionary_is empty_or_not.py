a=list(map(str,input('Enter the keywords : ').split()))
b=list(map(str,input('Enter the values : ').split()))
out=dict(zip(a,b))
print(out)
if out=={}:

    print('Given dictionary is empty')
else:
    print('Given dictionary is not empty')

def value(*a,j=' '):
    st=map(str,a)
    return j.join(st)
out=value(1,2,3,4,'helo','python')
print(out)
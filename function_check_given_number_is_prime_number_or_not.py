def prime(x):
    for i in range(2,x):
        if x%i==0:
            return 'Not prime number '
    else:
        return 'Entered number is a prime number'
num=int(input('Enter the number : '))
out=prime(num)
print(out)
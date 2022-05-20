lst=input("Enter the list of the elements : ")
lst1=list(map(str,lst.split()))
lst2=int(input("Enter the length of the list : "))
lst3=[]
print("Enter the values of the elements : ")
for i in range(0,lst2):
    elem=int(input())
    lst3.append(elem)
out=dict(zip(lst1,lst3))
print(out)
if out=={}:
    print("Enter dictionary is empty dictionary ")
else:
    print("Entered dictionary is not empty dictionary")
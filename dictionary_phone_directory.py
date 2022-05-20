Phonebook={}
number_of_contacts=int(input('Enter the number of cantacts : '))
for i in range(number_of_contacts):
    a,b=input().split()
    Phonebook[a]=b
print(Phonebook)
# method 1 to merge to dct by using mathematical ecxpression
dct={'Name':'vishnukant','rollno':56,'College name':'Gla university'}
dct1={'Name1':'jatin','rollno2':65,'College name3':'Gla university'}
out={**dct1,**dct}
print(out)

#method 2  to merge two dictionary  by using " | " between to dictinary
dct={'Name':'vishnukant','rollno':56,'College name':'Gla university'}
dct1={'Name1':'jatin','rollno2':65,'College name3':'Gla university'}
out=dct1|dct
print(out)

#method 3 to merge two dictionary by using .update function 
dct={'Name':'vishnukant','rollno':56,'College name':'Gla university'}
dct1={'Name1':'jatin','rollno2':65,'College name3':'Gla university'}
dct.update(dct1)
print(dct)


#question 1-
double = lambda x: x * 2
print(double(5))
#question 2-
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) ,my_list))
print(new_list)
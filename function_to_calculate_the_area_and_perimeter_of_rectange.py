def area_perimeter_of_rectangle(x,y):
    Area_of_rectangle=x*y
    perimeter_of_rectangle=2*(x+y)
    print('The area of rectange',Area_of_rectangle)
    print('The perimeter of rectangele : ',perimeter_of_rectangle)

length=eval(input('Enter the length of the rectangle : '))
breadth=eval(input('Enter the breadth of the rectangle : '))
area_perimeter_of_rectangle(length,breadth)

def area_circumference_circle(x):
    pie=3.14
    area_of_circle=pie*(x**2)
    circumference_circle=2*pie*x
    print('The area of circle : ',area_of_circle)
    print('The circumference of the circle : ',round(circumference_circle,2))
Radius_of_the_circle=eval(input('Enter the radius of the circle :' ))
area_circumference_circle(Radius_of_the_circle)
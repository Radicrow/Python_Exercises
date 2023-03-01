from math import pi

#Return the value of area and perimeter of a circle after inputing the radius

def circle(radius):
    area = radius**2 * pi
    per = radius * 2 * pi
    print("The area is " + str(area))
    print("The perimeter is " + str(per))

#Example
circle(5)
from abc import ABC,abstractmethod
import math
from turtle import *
import time
class Shape(ABC):
    @abstractmethod
    def __init__(self,colour,filled):
        self.colour = colour
        self.filled = filled
    @abstractmethod
    def area(self):
        pass
# defines attributes for the shapes
class Circle(Shape):
    def __init__(self,colour,filled,radius):
        super().__init__(colour,filled)
        self.radius = radius

    def area(self):
        circle_area = f"{math.pi * self.radius * self.radius:.2f}"
        return circle_area
    def perimeter(self):
        perimeter = f"{2 * math.pi * self.radius:.2f}"
        return perimeter
    def circle_drawing(self):
        pendown()
        pencolor(self.colour)
        goto(0,0)
        #uses built in circle drawing function
        if self.filled.lower() == "true":
            fillcolor(self.colour)
            begin_fill()
            circle(self.radius)
            end_fill()
        else:
            circle(self.radius)
class Triangle(Shape):
    def __init__(self,colour,filled,height,base):
        super().__init__(colour,filled)
        self.height = height
        self.base = base

    def area(self):
        triangle_area = f"{self.base * self.height/2:.2f}"
        return triangle_area
    def perimeter(self):
        perimeter = f"{self.base +self.slant_height + self.slant_height:.2f}"
        return perimeter
    def slant_height(self):
        slant_height = float(math.sqrt(((self.base*self.base)+(self.height*self.height))))
        return slant_height
    def triangle_isosceles_angle(self):
        # currently can only draw isosceles triangles
        triangle_isosceles_angle = math.degrees(float(math.atan(self.height/(self.base/2))))
        return triangle_isosceles_angle
    def triangle_drawing(self):
        pendown()
        pencolor(self.colour)
        goto(0,0)
        if self.filled.lower() == "true":
            fillcolor(self.colour)
            begin_fill()
            lt(180)
            fd(self.base//2)
            rt(180-self.triangle_isosceles_angle())
            fd(self.slant_height()//2)
            rt(180-(180-self.triangle_isosceles_angle()*2))
            fd(self.slant_height()//2)
            rt(180-self.triangle_isosceles_angle())
            fd(self.base // 2)
            end_fill()
        else:
            lt(180)
            fd(self.base // 2)
            #calculating angles of turn
            rt(180 - self.triangle_isosceles_angle())
            fd(self.slant_height() // 2)
            rt(180 - (180 - self.triangle_isosceles_angle() * 2))
            fd(self.slant_height() // 2)
            rt(180 - self.triangle_isosceles_angle())
            fd(self.base // 2)
class Square(Shape):
    def __init__(self, colour, filled, height):
        super().__init__(colour, filled)
        self.height = height

    def area(self):
        square_area = f"{self.height * self.height:.2f}"
        return square_area
    def perimeter(self):
        perimeter = f"{self.height * 4:.2f}"
        return perimeter
    def square_drawing(self):
        pendown()
        pencolor(self.colour)
        goto(0,0)
        if self.filled.lower() == "true":
            fillcolor(self.colour)
            begin_fill()
            #making pen face left and going forward half of the length
            lt(180)
            fd(self.height//2)
            #turns and lengths are equal, the for loop iterates the turns and length
            for i in range(3):
                rt(90)
                fd(self.height)
            #making pen only go half the distance again
            rt(90)
            fd(self.height//2)
            end_fill()
        else:
            # does same thing as before but without fill functions
            lt(180)
            fd(self.height // 2)
            for i in range(3):
                rt(90)
                fd(self.height)
            rt(90)
            fd(self.height // 2)
try:
    d = input("tell me which shape's area and perimeter you want to know: triangle, circle or square\n")
    if d.lower() not in ("circle", "triangle", "square"):
        raise ValueError
    else:
        match d.lower():
            case "circle":
                try:
                    c = input("what is the 'colour, is it filled?(true or false),radius' of the circle in that format\n")
                    l = [item.strip() for item in c.split(',')]
                    if len(l) != 3:
                        raise SyntaxError
                    if l[1].lower() not in ('true', 'false'):
                        raise SyntaxError
                    # making an aray of three elements, so each can be assigned to a variable
                    circle1 = Circle(l[0], l[1], float(l[2]))
                    # finding area
                    print(f"the area is {circle1.area()}cm squared\n")
                    print(f"the perimeter is {circle1.perimeter()}cm\n")
                    draw = input("would you like to draw your shape?")
                    if draw.lower() == "yes":
                        circle1.circle_drawing()
                        time.sleep(10)
                    else:
                        exit()
                except (SyntaxError, ValueError, IndexError):
                    print(
                        "please type in the format displayed with the correct syntax and restart the program\n")

            case "triangle":
                try:
                    t = input("what is the 'colour, is it filled?(true or false),height,base' of the triangle in that format\n")
                    b = [item.strip() for item in t.split(',')]
                    if len(b) != 4:
                        raise SyntaxError
                    if b[1].lower() not in ('true', 'false'):
                        raise SyntaxError
                    triangle = Triangle(b[0], b[1], float(b[2]), float(b[3]))
                    print(f"the area is {triangle.area()}cm squared\n")
                    print(f"the perimeter is {triangle.perimeter()}cm\n")
                    draw = input("would you like to draw your shape?\n")
                    if draw.lower() == "yes":
                        triangle.triangle_drawing()
                        time.sleep(10)
                    else:
                        exit()
                except (SyntaxError, ValueError, IndexError):
                    print("please type in the format displayed with the correct syntax and restart the program\n")
            case "square":
                try:
                    q = input("what is the 'colour, is it filled?(true or false),height' of the square in that format\n")
                    u = [item.strip() for item in q.split(',')]
                    if len(u) != 3:
                        raise SyntaxError
                    if u[1].lower() not in ('true', 'false'):
                        raise SyntaxError
                    square = Square(u[0], u[1], float(u[2]))
                    print(f"the area is {square.area()}cm squared\n")
                    print(f"the perimeter is {square.perimeter()}cm\n")
                    draw = input("would you like to draw your shape?\n")
                    if draw.lower() == "yes":
                        square.square_drawing()
                        time.sleep(10)
                    else:
                        exit()
                except (SyntaxError, ValueError, IndexError):
                    print("please type in the format displayed with the correct syntax and restart the program\n")
except ValueError:
    print("please type in the format displayed with the correct syntax and restart the program\n")

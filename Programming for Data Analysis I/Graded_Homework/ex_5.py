#import math for tangent, square root and pi
import math


#Using inheritance whenever possible, write a module shapes.py that contains the following classes:
#1)Parallelogram, with the following attributes:
#height
#● width (the base length)
#● height (the distance between the two bases)
#● corner (the position of the bottom left corner in the plane)
##● angle (the angle between the base and one of its adjacent sides)
#2)Rectangle (a special case of Parallelogram with angle=pi/2)
# 3)Square (a special case of Rectangle with width=height)
#All classes must have the following methods:
#● __init__, __str__, area, perimeter;
#● move, that takes dx and dy and updates the corner by adding (dx, dy);
#● get_corners, that returns the four corners of the shape (as Point objects).
#Finally, shapes.py must also contain the (polymorphic) function check_overlap that takes any two shapes and verify whether they overlap.


#creates a point object 
class Point:
    
    '''Creates a point in 2D space'''

    def __init__(self, x = 0,y = 0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '({},{})'.format(self.x,self.y)
    
    def __add__(self,other):
        r = Point()
        r.x = self.x + other.x
        r.y = self.y + other.y
        return r
    
    def compute_distance(self,other):
        return math.sqrt((self.x - other.x)**2+(self.y - other.y)**2)

class Parallelogram:
    
    '''creates a parallelogram object with height, width, angle size and corner {a point object on the lower left side of the shape}'''

    def __init__(self, height = 1, width = 1, angle = 90, corner = None ):

        self.height = height
        self.width = width
        
        if corner is None:
            self.corner = Point()
        else:
            self.corner = corner
        
        self.angle = angle
    
    def __str__(self):
        
        return 'Parallelogram Height: {}\nParallelogram Width: {}\nParallelogram Angle: {}\n'.format(self.height,self.width,self.angle)
    
    def area(self):
        
        return self.height * self.width

    def perimeter(self):
        
        point_a = self.corner
        print(point_a)
        point_d = point_a + Point(self.height/math.tan(self.angle),self.height)
        print(point_d)
        a_to_d =  Point.compute_distance(point_a,point_d)
        perimeter = a_to_d *2 + self.width*2
        
        return perimeter

    
    def move(self,dx,dy):
        self.corner.x += dx
        self.corner.y += dy

        return self.corner.x, self.corner.y

    def get_corner(self):
        #
        #   D           C
        #    /---------/
        #   / |       /
        #  /---------/
        # A   D      B          AD = Small base

        #if the angle is math.pi/2 which means its a rectangle or a square, we dont need to find the side
        if self.angle == math.pi / 2:
            smallbase = 0
            #creates a point object for all corners ABCD
            A = self.corner
            B = A + Point(self.width,0)
            C = B + Point(smallbase, self.height)
            D = A + Point(smallbase, self.height)
            return A,B,C,D 
        
        else:
            #the smallbase has the formula height/tangent(angle)
            smallbase = self.height/math.tan(self.angle)
            #creates a point object for all corners ABCD
            A = self.corner
            B = A + Point(self.width,0)
            C = B + Point(smallbase, self.height)
            D = A + Point(smallbase, self.height)
            return A,B,C,D
    

class Rectangle(Parallelogram):

    ''' Creates a Rectangle object, Inherits almost everything from the parallelogram class '''
    
    def __init__(self,height =1 , width = 1, corner = None):
        
        self.height = height
        self.width = width

        if corner is None:
            self.corner = Point()
        else:
            self.corner = corner

        self.angle = math.pi/2
        
    def __str__(self):
        
        return 'Rectangle Height: {}\nRectangle Width: {}\nRectangle Angle: {}\n'.format(self.height,self.width,self.angle)
    
    def area(self):
        
        return self.height * self.width
    
    def perimeter(self):
        return ((2 * self.height) + (self.width * 2))

    

    

class Square(Rectangle):
    '''Creates a Square object, inherits everything from the rectangle and the parallelogram'''

    def __init__(self, side = 1, corner = None):
       
        self.height = side
        self.width = side
        
        if corner is None:
            self.corner = Point()
        else:
            self.corner = corner

        self.angle = math.pi/2
    
    def __str__(self):
        
        return 'Square Side: {}\nSquare Angle: {}\n'.format(self.height,self.angle)
    
#have not figured out whether the function should be inside or outside the class, i'll comment the function that works from inside the rectangle classe whilst having the one that works with two rectangle objects outside the clases
#     
#def check_overlap_rectangles(self,shape2):
    
    #separating axis theorem
#        a1,a2,a3,a4 = self.get_corner()
#        b1,b2,b3,b4 = shape2.get_corner()
    
#        return not(a3.x < b1.x or a1.x > b3.x or a3.y < b1.y or a1.y >b3.y)

def check_overlap_rectangles(shape1,shape2):
    
        #unpacks all the points from the get_corner from the two shapes
        #
        # D |---------| C
        #   |         |
        #   |         |
        #   |---------|
        # A             B
        
        #unpacks the points, we dont need all of them but we might aswell unpack them all since its easier and faster
        a1,a2,a3,a4 = shape1.get_corner()
        b1,b2,b3,b4 = shape2.get_corner()
        #separating axis theorem
        return not(a3.x < b1.x or a1.x > b3.x or a3.y < b1.y or a1.y > b3.y)



point_a = Point(0,0)
point_b = Point(11,5)

p = Parallelogram(10,5,180,point_a)
print(p)
print('parallelogram area and perimeter:', p.area(),p.perimeter())
a,b,c,d = p.get_corner()
print('corner', a,b,c,d)

r = Rectangle(10,10,point_a)
print(r)
print('rectangle area and perimeter:',r.area(),r.perimeter())
a,b,c,d = r.get_corner()
print(a,b,c,d)

s = Square(10,point_b)
print(s)
print('square area and perimeter:',s.area(),s.perimeter())
a,b,c,d = s.get_corner()
print(a,b,c,d)


print(check_overlap_rectangles(r,s))

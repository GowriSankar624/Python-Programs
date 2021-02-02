import graphics.rectangle
print("Rectangle")
l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
print("Area: ",graphics.rectangle.area(l,b))
print("perimeter: ",graphics.rectangle.perimeter(l,b))


from graphics.circle import area as a
from graphics.cicrle import perimeter as p
print("\nCircle")
r=int(input("enter the radius: "))
print("area:", a(r))
print("perimeter:",p(r))

      
      
from graphics.dgraphics.cubiod import area as a
from graphics.dgraphics.cubiod import perimeter as p
print("\nCuboid")
l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
h=int(input("enter the height:"))
print("area:",a(l,b,h))
print("perimeter:",p(1,b,h))



from graphics.dgraphics.sphere import*
print("\nSphere")
r=int(input("enter the radius of sphere:"))
print("area:",area(r))
print("circumference of sphere:",cirucmference(r))

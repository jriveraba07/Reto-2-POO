# Clear una clase rectangulo con estos parametros:
#* The rectangle should be inicialice using any of these 3 methods:

#* Method 1: Bottom-left corner(Point) + width and height
#todo Method 2: Center(Point) + width and height
#todo Method 3: Two opposite corners (Points) e.g. Bottom-left and Upper-right

#* width, height, center: Instance attributes

#* compute_area(): should return the area of the rectangle

#* compute_perimeter(): should return the perimeter of the rectangle

class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
  def move(self, new_x, new_y):
    self.x = new_x
    self.y = new_y
  def reset(self):
    self.x = 0
    self.y = 0

class Rectangle_M1():
    def __init__(self, point_blc : "Point", width: float, height: float):
        self.width = width
        self.height = height
        self.pointc = Point(x = (point_blc.x + width) / 2, y = (point_blc.x + height) / 2 )
    
    def compute_area(self)-> float:
        return self.width * self.height
    
    def compute_perimeter(self)-> float:
        return (2 * self.width) + (2 * self.height)

    def computer_interference_point(self, pointint : "Point")-> bool:
        a : float = self.width/2
        b : float = self.height/2
        return self.pointc.x - a < pointint.x < self.pointc.x + a and self.pointc.y - b < pointint.y < self.pointc.y + b 

class Square(Rectangle_M1):
    def __init__(self, point_blc : "Point", side: float):
        super().__init__(point_blc, width = side, height = side)


point_1 = Point(1, 1)
rectangle = Rectangle_M1(point_1, width = 2, height = 3)

print("La base del rectangulo es:", rectangle.width)
print("La altura del rectangulo es:", rectangle.height)
print("el centro del rectangulo esta ubicado en:", f"({rectangle.pointc.x} , {rectangle.pointc.y})")
print("El area del rectangulo es:", rectangle.compute_area())
print("El perimetro del rectangulo es:", rectangle.compute_perimeter())

cuadrado = Square(point_1, side = 3)

print("El cuadrado: ")
print("el cuadrado en cuention tiene")
print(f"Altura de ({cuadrado.width}) y base de ({cuadrado.height}) ")
print(f"Area de ({cuadrado.compute_area()}) y base de ({cuadrado.compute_perimeter()}) ")

print(cuadrado.computer_interference_point(Point(3, 3)))

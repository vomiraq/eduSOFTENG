# создаем класс Shape (фигура) - это базовый класс для полиморфизма.
class Shape:
    
    # определяем метод area (площадь), который будет переопределен.
    # пока он пустой (pass).
    def area(self):
        pass

# создаем класс Rectangle (прямоугольник), наследуем его от Shape.
class Rectangle(Shape):
    
    # конструктор для прямоугольника, принимает ширину (width) и высоту (height).
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # переопределяем метод area() для расчета площади прямоугольника.
    def area(self):
        return self.width * self.height

# создаем класс Circle (круг), наследуем его от Shape.
class Circle(Shape):
    
    # конструктор для круга, принимает радиус (radius).
    def __init__(self, radius):
        self.radius = radius

    # переопределяем метод area() для расчета площади круга.
    # используем 3.14 как приближенное значение Пи.
    def area(self):
        return 3.14 * self.radius * self.radius

# создаем объекты разных классов, но они все являются "фигурами" (Shape).
rectangle = Rectangle(width=10, height=5)
circle = Circle(radius=7)

# создаем массив (список) и помещаем туда фигуры.
shapes = [rectangle, circle]
...
print("Расчет площади фигур")

# с помощью цикла обходим массив.
# здесь проявляется полиморфизм: для каждой фигуры вызывается свой метод area().
for shape in shapes:
    # у прямоугольника вызовется Rectangle.area(), у круга - Circle.area().
    print(f"Площадь {shape.__class__.__name__}: {shape.area()}")
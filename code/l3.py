# создаем класс Car (автомобиль) из предыдущих заданий.
class Car:
    
    # конструктор.
    def __init__(self, make, model):
        self.make = make 
        self.model = model

    # метод "поехать".
    def drive(self):
        print(f"Driving the {self.make} {self.model}")

# создаем класс ElectricCar, который наследуется от Car.
# это значит, что ElectricCar получит все методы и атрибуты класса Car.
class ElectricCar(Car): 
    
    # конструктор для электромобиля. добавляем новый параметр battery_capacity.
    def __init__(self, make, model, battery_capacity):
        
        # вызываем конструктор родительского класса (Car) через super().
        # это нужно, чтобы инициализировать make и model.
        super().__init__(make, model)
        
        # записываем емкость батареи, это собственный атрибут ElectricCar.
        self.battery_capacity = battery_capacity 

    # новый метод charge (заряжаться).
    def charge(self):
        # выводим сообщение о зарядке, используя все атрибуты.
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh battery.")

# создаем объект 'my_electric_car', теперь это Tesla Model S.
my_electric_car = ElectricCar("Tesla", "Model S", 75)

# заставляем машину "поехать" (используем унаследованный метод).
my_electric_car.drive()

# заставляем машину "заряжаться" (используем собственный метод).
my_electric_car.charge()
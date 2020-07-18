# 파이썬 클래스
# 상속, 다중상속

class Car:
    """Parent Class"""
    def __init__(self, type, color):
        self.type = type
        self.color = color

    def show(self):
        return 'Car Class show()'

class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, type, color):
        super().__init__(type, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, type, color):
        super().__init__(type, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name
    
    def show(self):
        print(super().show())
        return "Car Info : %s %s %s" %(self.car_name, self.type, self.color) 
        
# Use
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color)
print(model1.type)
print(model1.car_name)
print(model1.show())
print(model1.show_model())
print(model1.__dict__)
print()

# Method Overriding
model2 = BenzCar("s", "suv", "black")
print(model2.show())
print()

# Parent Method call
model3 = BenzCar("c", "sedan", "blue")
print(model3.show())
print()

# Inheritance
print(BmwCar.mro())
print(BenzCar.mro())
print()
print()

# 다중상속
class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y,Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())
class Car:
    def __init__(self,detail):
        self.detail=detail
    def print(self):
        print(self.detail)
class CarFactory:
    def createFordCar(self):
       details=[1995,'Mustang']
       return Car(details)
    def createAudiCar(self):
        details=[2000,'Q7']
        return Car(details)
car=CarFactory()
car.createFordCar().print()
car.createAudiCar().print()


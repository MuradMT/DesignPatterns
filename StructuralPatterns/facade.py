class SubSystemOne:
    def MethodOne(self):
        print('SubSystemOne Method')
class SubSystemTwo:
    def MethodTwo(self):
        print('SubSystemTwo Method')
class SubSystemThree:
    def MethodThree(self):
        print('SubSystemThree Method')
class SubSystemFour:
    def MethodFour(self):
        print('SubSystemFour Method')
class Facade:
    def __init__(self):
        self.one=SubSystemOne()
        self.two=SubSystemTwo()
        self.three=SubSystemThree() 
        self.four=SubSystemFour()
    def MethodA(self):
        self.one.MethodOne()
        self.two.MethodTwo()
        self.four.MethodFour() 
    def MethodB(self):
        self.two.MethodTwo()
        self.three.MethodThree()
facade=Facade()
facade.MethodA()
facade.MethodB()

        
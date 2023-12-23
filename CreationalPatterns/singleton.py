class ApplicationState:
    instance=None
    def __init__(self):
        self.isLoggedIn=False
    def publicMethod(self):
        print('This is public method')
    def __privateMethod(self):#in python,private methods are created with adding __ before the method name
        print('This is private method')
    @staticmethod
    def getAppState():
        if not ApplicationState.instance:
            ApplicationState.instance=ApplicationState()
        return ApplicationState.instance
appState1=ApplicationState.getAppState()
appState2=ApplicationState.getAppState()
app=ApplicationState()
appState1.isLoggedIn=True
appState1.__privateMethod()#raise error
print(appState1.isLoggedIn)
print(appState2.isLoggedIn)
print(app.isLoggedIn)
#in python,you can not create private constructor

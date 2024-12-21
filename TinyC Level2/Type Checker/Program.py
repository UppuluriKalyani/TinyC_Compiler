class Program:
    def __init__(self):
        self.functions = {}

    def addFunctionDetails(self, name, function):
        self.functions[name] = function

    def print(self):
        print("Program:")
        for name in self.functions.keys():
            self.functions[name].print()

    def getMainFunction(self):
        for funname, function in self.functions.items():
            if funname == 'main':
                return function

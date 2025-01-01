class Program:
    def __init__(self):
        self.functions = {}

    def addFunctionDetails(self, name, function):
        self.functions[name] = function

    def print(self):
        print("Program:")
        for fun_name in self.functions.keys():
            self.functions[fun_name].print()

    def getMainFunction(self):
        for fun_name in self.functions.keys():
            if fun_name == 'main':
                return self.functions[fun_name]

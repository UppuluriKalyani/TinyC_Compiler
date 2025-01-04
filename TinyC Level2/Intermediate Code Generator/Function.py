from SymbolTable import SymbolTable

class Function:
    def __init__(self, returnType, name):
        self.returnType = returnType
        self.name = name
        self.intermediateCodeList = []
        self.localSymbolTable = SymbolTable()

    def setIntermediateCodeList(self, icodeList):
        self.intermediateCodeList = icodeList

    def getIntermediateCodeList(self):
        return self.intermediateCodeList

    def setLocalSymbolTable(self, localList):
        self.localSymbolTable = localList

    def getLocalSymbolTable(self):
        return self.localSymbolTable

    def print(self):
        print(f"Procedure: {self.name}, Return Type: {self.returnType}\n")
        print("3-address code:")
        for i in self.intermediateCodeList:
            i.print()

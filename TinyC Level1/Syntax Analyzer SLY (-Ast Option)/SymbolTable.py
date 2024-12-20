from enum import Enum

DataType = Enum('DataType', ['INT', 'DOUBLE'])

class SymbolTableEntry:
    def __init__(self, name, datatype):
        self.name = name
        self.datatype = datatype
        self.value = None

    def getSymbolName(self):
        return self.name

    def getDataType(self):
        return self.datatype

    def print(self):
        print(f'Name: {self.name}, DataType: {self.datatype}, Value: {self.value}')

class SymbolTable:
    def __init__(self):
        self.table = []

    def addSymbol(self, symbol):
        self.table.append(symbol)

    def nameInSymbolTable(self, name):
        for symb in self.table:
            if symb.getSymbolName() == name:
                return True
        return False

    def getSymbolEntry(self, name):
        for i in self.table:
            if i.name == name:
                return i

    def printSymbolTable(self):
        for i in self.table:
            i.print()

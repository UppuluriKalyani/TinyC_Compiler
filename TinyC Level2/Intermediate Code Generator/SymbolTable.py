from enum import Enum

DataType = Enum('DataType', ['INT', 'DOUBLE'])


class SymbolTableEntry:
    def __init__(self, name, datatype):
        self.name = name
        self.datatype = datatype

    def getSymbolName(self):
        return self.name

    def getDataType(self):
        return self.datatype

    def print(self):
        print(f"name: {self.name}\tdatatype: {self.datatype}")


class SymbolTable:
    def __init__(self):
        self.table = []

    def addSymbol(self, symbol):
        self.table.append(symbol)

    def nameInSymbolTable(self, name):
        for entry in self.table:
            if entry.getSymbolName() == name:
                return True
        return False

    def getSymbolInTable(self, name):
        for entry in self.table:
            if entry.getSymbolName() == name:
                return entry

    def printSymbolTable(self):
        for symbol in self.table:
            symbol.print()

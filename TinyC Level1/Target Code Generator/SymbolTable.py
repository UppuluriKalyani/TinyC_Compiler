from enum import Enum

DataType = Enum("DataType", ["INT", "DOUBLE"])

class SymbolTableEntry:
    def __init__(self, name, datatype, offset, value=None):
        self.name = name
        self.datatype = datatype
        self.value = value
        self.offset = offset

    def getSymbolName(self):
        return self.name

    def getOffset(self):
        return self.offset

    def getDataType(self):
        return self.datatype

    def addDataType(self, type):
        self.datatype = type

    def print(self):
        print(f"Name = {self.name}, DataType = {self.datatype}, Offset = {self.offset}, Value = {self.value}")


class SymbolTable:
    def __init__(self):
        self.table = []

    def addSymbol(self, symbol):
        self.table.append(symbol)

    def nameInSymbolTable(self, name):
        for i in self.table:
            if i.getSymbolName() == name:
                return True
        return False

    def getSymbol(self, name):
        for i in self.table:
            if i.getSymbolName() == name:
                return i
        return None

    def getLen(self):
        return len(self.table)

    def printSymbolTable(self):
        for symbol in self.table:
            symbol.print()

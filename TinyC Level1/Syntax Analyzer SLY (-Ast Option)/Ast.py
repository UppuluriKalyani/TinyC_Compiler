from enum import Enum
from abc import ABCMeta, abstractmethod
from SymbolTable import SymbolTable

DataType = Enum('DataType', ['INT', 'DOUBLE'])

class AST(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def typeCheckAST(self):
        pass

    @abstractmethod
    def getDataType(self):
        pass

class NumberAst(AST):
    def __init__(self, number):
        self.value = number

    def print(self):
        print(f"Num: {self.value}", end="")

    def getDataType(self):
        return type(self.value)

    def typeCheckAST(self):
        pass

class NameAst(AST):
    def __init__(self, symbolEntry):
        self.symbolEntry = symbolEntry

    def print(self):
        print(f"Name: {self.symbolEntry}", end="")

    def getDataType(self):
        return SymbolTable.getSymbolEntry(self.symbolEntry).getDataType()

    def typeCheckAST(self):
        pass

class AssignAst(AST):
    def __init__(self, left, right, lineNo):
        self.left = left
        self.right = right
        self.lineNo = lineNo

    def getDataType(self):
        pass

    def typeCheckAST(self):
        if self.left.getDataType() == self.right.getDataType():
            return True
        else:
            return False

    def print(self):
        print("\t\tAsgn:")
        print("\t\t\tLHS (", end="")
        self.left.print()
        print(")")
        print("\t\t\tRHS (", end="")
        self.right.print()
        print(")")

class PrintAst(AST):
    def __init__(self, symbolEntry):
        self.symbolEntry = symbolEntry

    def print(self):
        print("\t\tPrint:")
        print(f"\t\t\t", end="")
        self.symbolEntry.print()
        print()

    def getDataType(self):
        pass

    def typeCheckAST(self):
        pass

from Ast import *
from SymbolTable import *

class Function:
    def __init__(self, returnType, name):
        self.returnType = returnType
        self.name = name
        self.statementsAstList = []
        self.localSymbolTable = SymbolTable()

    def setStatementsAstList(self, sastList):
        self.statementsAstList = sastList

    def getStatementsAstList(self):
        return self.statementsAstList

    def setLocalSymbolTable(self, localList):
        self.localSymbolTable = localList

    def getLocalSymbolTable(self):
        return self.localSymbolTable

    def print(self):
        print(f"\tProcedure: {self.name} Return type: {self.returnType}")
        for statement in self.getStatementsAstList():
            if statement is not None:
                statement.print()

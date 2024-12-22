from enum import Enum
from abc import ABCMeta, abstractmethod

# Enum for DataType
DataType = Enum('DataType', ['INT', 'DOUBLE'])

# Abstract Syntax Tree (AST) Base Class
class AST(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass

    def typeCheckAST(self):
        pass

    def getDataType(self):
        pass

# NumberAst Class
class NumberAst(AST):
    def __init__(self, number):
        self.value = number

    def getNumber(self):
        return self.value

    def print(self):
        print(f'Number : {self.value}', end='')

    def getDataType(self):
        if isinstance(self.value, int):
            return DataType.INT.name
        elif isinstance(self.value, float):
            return DataType.DOUBLE.name

# NameAst Class
class NameAst(AST):
    def __init__(self, symbolEntry):
        self.symbolEntry = symbolEntry

    def getSymbolEntry(self):
        return self.symbolEntry

    def print(self):
        print(f"NameAst : {self.symbolEntry.getSymbolName()}", end="")

    def getDataType(self):
        return self.symbolEntry.getDataType()

# Arithmetic AST Classes
class AdditionAst(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def getDataType(self):
        if self.left.getDataType() == self.right.getDataType():
            return self.left.getDataType()
        return None

    def print(self):
        print("\nAdditionAst:\n\tLHS (", end="")
        self.left.print()
        print(')\n\tRHS (', end="")
        self.right.print()
        print(")")

class SubtractionAst(AdditionAst):
    def print(self):
        print("\nSubtractionAst:\n\tLHS (", end="")
        self.left.print()
        print(')\n\tRHS (', end="")
        self.right.print()
        print(")")

class MultiplicationAst(AdditionAst):
    def print(self):
        print("\nMultiplicationAst:\n\tLHS (", end="")
        self.left.print()
        print(')\n\tRHS (', end="")
        self.right.print()
        print(")")

class DivisionAst(AdditionAst):
    def print(self):
        print("\nDivisionAst:\n\tLHS (", end="")
        self.left.print()
        print(')\n\tRHS (', end="")
        self.right.print()
        print(")")

class ModAst(AdditionAst):
    def print(self):
        print("\nModAst:\n\tLHS (", end="")
        self.left.print()
        print(')\n\tRHS (', end="")
        self.right.print()
        print(")")

# Relational AST Classes
class GreaterAst(AdditionAst):
    def print(self):
        print("\nGreaterAst:\n\tLHS (", end="")
        self.left.print()
        print(')\n\tRHS (', end="")
        self.right.print()
        print(")")

class LessThanAst(AdditionAst):
    def print(self):
        print("\nLessThanAst:\n\tLHS (", end="")
        self.left.print()
        print(')\n\tRHS (', end="")
        self.right.print()
        print(")")

class GreaterEqualAst(AdditionAst):
    def print(self):
        print("\nGreaterEqualAst:\n\tLHS (", end="")
        self.left.print()
        print(')\n\tRHS (', end="")
        self.right.print()
        print(")")

class LessEqualAst(AdditionAst):
    def print(self):
        print("\nLessEqualAst:\n\tLHS (", end="")
        self.left.print()
        print(')\n\tRHS (', end="")
        self.right.print()
        print(")")

class EqualAst(AdditionAst):
    def print(self):
        print("\nEqualAst:\n\tLHS (", end="")
        self.left.print()
        print(')\n\tRHS (', end="")
        self.right.print()
        print(")")

class NotEqualAst(AdditionAst):
    def print(self):
        print("\nNotEqualAst:\n\tLHS (", end="")
        self.left.print()
        print(')\n\tRHS (', end="")
        self.right.print()
        print(")")

# Logical AST Classes
class LogicalAnd(AdditionAst):
    def print(self):
        print("\nLogicalAnd:\n\tLHS (", end="")
        self.left.print()
        print(')\n\tRHS (', end="")
        self.right.print()
        print(")")

class LogicalOR(AdditionAst):
    def print(self):
        print("\nLogicalOR:\n\tLHS (", end="")
        self.left.print()
        print(')\n\tRHS (', end="")
        self.right.print()
        print(")")

# AssignAst Class
class AssignAst(AST):
    def __init__(self, left, right, lineNo):
        self.left = left
        self.right = right
        self.lineNo = lineNo

    def getDataType(self):
        if self.left.getDataType() == self.right.getDataType():
            return self.left.getDataType()
        return None

    def typeCheckAST(self):
        return self.left.getDataType() == self.right.getDataType()

    def print(self):
        print("\nAssignAst:\n\tLHS (", end="")
        self.left.print()
        print(')\n\tRHS (', end="")
        self.right.print()
        print(")")

from enum import Enum
from abc import ABCMeta, abstractmethod

DataType = Enum('DataType', ['INT', 'DOUBLE'])

class AST(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass

    def typeCheckAST(self):
        pass

    def getDataType(self):
        pass


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
        if isinstance(self.value, float):
            return DataType.DOUBLE.name


class NameAst(AST):
    def __init__(self, symbolEntry):
        self.symbolEntry = symbolEntry

    def getSymbolEntry(self):
        return self.symbolEntry

    def print(self):
        print(f"NameAst : {self.symbolEntry.getSymbolName()}", end="")

    def getDataType(self):
        return self.symbolEntry.getDataType()


class AdditionAst(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def getDataType(self):
        if self.left.getDataType() == self.right.getDataType():
            return self.left.getDataType()
        return self.left.getDataType()

    def print(self):
        print("\n\t\t\t\tAdditionAst :\n\t\t\t\t\tLHS (", end="")
        self.left.print()
        print(')\n\t\t\t\t\tRHS (', end="")
        self.right.print()
        print(")", end="\n\t\t\t\t")


class SubtractionAst(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def getDataType(self):
        if self.left.getDataType() == self.right.getDataType():
            return self.left.getDataType()

    def print(self):
        print("\n\t\t\t\tSubtractionAst :\n\t\t\t\t\tLHS (", end="")
        self.left.print()
        print(')\n\t\t\t\t\tRHS (', end="")
        self.right.print()
        print(")", end="\n\t\t\t\t")


class MultiplicationAst(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def getDataType(self):
        if self.left.getDataType() == self.right.getDataType():
            return self.left.getDataType()

    def print(self):
        print("\n\t\t\t\tMultiplicationAst :\n\t\t\t\t\tLHS (", end="")
        self.left.print()
        print(')\n\t\t\t\t\tRHS (', end="")
        self.right.print()
        print(")", end="\n\t\t\t\t")


class DivisionAst(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def getDataType(self):
        if self.left.getDataType() == self.right.getDataType():
            return self.left.getDataType()

    def print(self):
        print("\n\t\t\t\tDivisionAst :\n\t\t\t\t\tLHS (", end="")
        self.left.print()
        print(')\n\t\t\t\t\tRHS (', end="")
        self.right.print()
        print(")", end="\n\t\t\t\t")


class ModAst(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def getDataType(self):
        if self.left.getDataType() == self.right.getDataType():
            return self.left.getDataType()

    def print(self):
        print("\n\t\t\t\tModAst :\n\t\t\t\t\tLHS (", end="")
        self.left.print()
        print(')\n\t\t\t\t\tRHS (', end="")
        self.right.print()
        print(")", end="\n\t\t\t\t")


# Relational ASTs
class GreaterAst(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def getDataType(self):
        if self.left.getDataType() == self.right.getDataType():
            return self.left.getDataType()

    def print(self):
        print("\n\t\t\t\tGreaterAst :\n\t\t\t\t\tLHS (", end="")
        self.left.print()
        print(')\n\t\t\t\t\tRHS (', end="")
        self.right.print()
        print(")", end="\n\t\t\t\t")


class LessThanAst(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def getDataType(self):
        if self.left.getDataType() == self.right.getDataType():
            return self.left.getDataType()

    def print(self):
        print("\n\t\t\t\tLessThanAst :\n\t\t\t\t\tLHS (", end="")
        self.left.print()
        print(')\n\t\t\t\t\tRHS (', end="")
        self.right.print()
        print(")", end="\n\t\t\t\t")


class GreaterEqualAst(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def getDataType(self):
        if self.left.getDataType() == self.right.getDataType():
            return self.left.getDataType()

    def print(self):
        print("\n\t\t\t\tGreaterEqualAst :\n\t\t\t\t\tLHS (", end="")
        self.left.print()
        print(')\n\t\t\t\t\tRHS (', end="")
        self.right.print()
        print(")", end="\n\t\t\t\t")


class LessEqualAst(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def getDataType(self):
        if self.left.getDataType() == self.right.getDataType():
            return self.left.getDataType()

    def print(self):
        print("\n\t\t\t\tLessEqualAst :\n\t\t\t\t\tLHS (", end="")
        self.left.print()
        print(')\n\t\t\t\t\tRHS (', end="")
        self.right.print()
        print(")", end="\n\t\t\t\t")


class EqualAst(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def getDataType(self):
        if self.left.getDataType() == self.right.getDataType():
            return self.left.getDataType()

    def print(self):
        print("\n\t\t\t\tEqualAst :\n\t\t\t\t\tLHS (", end="")
        self.left.print()
        print(')\n\t\t\t\t\tRHS (', end="")
        self.right.print()
        print(")", end="\n\t\t\t\t")


class NotEqualAst(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def getDataType(self):
        if self.left.getDataType() == self.right.getDataType():
            return self.left.getDataType()

    def print(self):
        print("\n\t\t\t\tNotEqualAst :\n\t\t\t\t\tLHS (", end="")
        self.left.print()
        print(')\n\t\t\t\t\tRHS (', end="")
        self.right.print()
        print(")", end="\n\t\t\t\t")


# Logical ASTs
class LogicalAnd(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def getDataType(self):
        if self.left.getDataType() == self.right.getDataType():
            return self.left.getDataType()

    def print(self):
        print("\n\t\t\t\tLogicalAnd :\n\t\t\t\t\tLHS (", end="")
        self.left.print()
        print(')\n\t\t\t\t\tRHS (', end="")
        self.right.print()
        print(")", end="\n\t\t\t\t")


class LogicalOr(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def getDataType(self):
        if self.left.getDataType() == self.right.getDataType():
            return self.left.getDataType()

    def print(self):
        print("\n\t\t\t\tLogicalOr :\n\t\t\t\t\tLHS (", end="")
        self.left.print()
        print(')\n\t\t\t\t\tRHS (', end="")
        self.right.print()
        print(")", end="\n\t\t\t\t")


class AssignAst(AST):
    def __init__(self, left, right, lineNo):
        self.left = left
        self.right = right
        self.lineNo = lineNo

    def getDataType(self):
        if self.left.getDataType() == self.right.getDataType():
            return self.left.getDataType()

    def typeCheckAST(self):
        return self.left.getDataType() == self.right.getDataType()

    def print(self):
        print("\t\tAssignAst:\n\t\t\tLHS (", end="")
        self.left.print()
        print(')\n\t\t\tRHS (', end="")
        self.right.print()
        print(")")


class PrintAst(AST):
    def __init__(self, right):
        self.right = right

    def print(self):
        print("\t\tPrintAst: ")
        print("\t\t\t(", end="")
        self.right.print()
        print(')')

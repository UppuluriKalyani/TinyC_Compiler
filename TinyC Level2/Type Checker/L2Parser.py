from sly import Parser
from L2Lexer import LexicalAnalyzer
from SymbolTable import SymbolTable, SymbolTableEntry
from Ast import *
from Program import Program
from Function import Function
from enum import Enum

# Define DataType Enum
DataType = Enum("DataType", ["INT", "DOUBLE"])

class Level2Parser(Parser):
    # Lexer components
    literals = LexicalAnalyzer.literals
    tokens = LexicalAnalyzer.tokens

    # Operator precedence
    precedence = (
        ("left", "="),
        ("left", LOGICALOR),
        ("left", LOGICALAND),
        ("left", EQUAL, NOTEQUAL),
        ("left", "<", ">", GREATEREQUAL, LESSEQUAL),
        ("left", "+", "-"),
        ("left", "*", "/", "%"),
        ("right", UMINUS),
    )

    # Initialize global components
    program = Program()
    localSymbolTable = SymbolTable()
    dataType = None
    isAccepted = True

    @_('return_type ID "(" ")" "{" statements "}"')
    def Program(self, value):
        function = Function(value.return_type, value.ID)
        function.setStatementsAstList([i for i in value.statements if i is not None])
        function.setLocalSymbolTable(self.localSymbolTable)
        self.program.addFunctionDetails(value.ID, function)
        return self.isAccepted

    @_('INT')
    def return_type(self, value):
        return DataType.INT.name

    @_('DOUBLE')
    def return_type(self, value):
        return DataType.DOUBLE.name

    @_('statement ";" statements')
    def statements(self, value):
        return [value.statement] + value.statements

    @_('statement ";"')
    def statements(self, value):
        return [value.statement]

    @_('declaration')
    def statement(self, value):
        pass

    @_('assignment', 'print')
    def statement(self, value):
        return value[0]

    @_('type LIST')
    def declaration(self, value):
        pass

    @_('ID "," LIST')
    def LIST(self, value):
        self.localSymbolTable.addSymbol(SymbolTableEntry(value.ID, self.dataType, self.localSymbolTable.getLen() * -4))

    @_('ID "=" NUMBER "," LIST')
    def LIST(self, value):
        self.localSymbolTable.addSymbol(SymbolTableEntry(value.ID, self.dataType, self.localSymbolTable.getLen() * -4, value.NUMBER))

    @_('ID "=" NUMBER')
    def LIST(self, value):
        self.localSymbolTable.addSymbol(SymbolTableEntry(value.ID, self.dataType, self.localSymbolTable.getLen() * -4, value.NUMBER))

    @_('ID')
    def LIST(self, value):
        self.localSymbolTable.addSymbol(SymbolTableEntry(value.ID, self.dataType, self.localSymbolTable.getLen() * -4))

    @_('ID "=" expr')
    def assignment(self, value):
        if self.localSymbolTable.nameInSymbolTable(value.ID):
            lhs = NameAst(self.localSymbolTable.getSymbol(value.ID))
            ast = AssignAst(lhs, value.expr, value.lineno)
            if value.expr is not None:
                if ast.typeCheckAST():
                    return ast
                else:
                    print(f"Type mismatch at line {value.lineno}")
                    self.isAccepted = False
                    return None
        else:
            print(f"Symbol {value.ID} not declared")
            self.isAccepted = False
            return None

    @_('PRINT expr')
    def print(self, value):
        return PrintAst(value.expr)

    # Binary operations
    @_(
        'expr "+" expr',
        'expr "-" expr',
        'expr "*" expr',
        'expr "/" expr',
        'expr "%" expr',
        'expr ">" expr',
        'expr "<" expr',
        'expr GREATEREQUAL expr',
        'expr LESSEQUAL expr',
        'expr EQUAL expr',
        'expr NOTEQUAL expr',
        'expr LOGICALAND expr',
        'expr LOGICALOR expr',
    )
    def expr(self, value):
        operators = {
            "+": AdditionAst,
            "-": SubtractionAst,
            "*": MultiplicationAst,
            "/": DivisionAst,
            "%": ModAst,
            ">": GreaterAst,
            "<": LessThanAst,
            ">=": GreaterEqualAst,
            "<=": LessEqualAst,
            "==": EqualAst,
            "!=": NotEqualAst,
            "&&": LogicalAndAst,
            "||": LogicalOrAst,
        }
        return operators[value[1]](value.expr0, value.expr1)

    @_('NUMBER')
    def expr(self, value):
        return NumberAst(value.NUMBER)

    @_('FLOAT')
    def expr(self, value):
        return NumberAst(value.FLOAT)

    @_('ID')
    def expr(self, value):
        if self.localSymbolTable.nameInSymbolTable(value.ID):
            return NameAst(self.localSymbolTable.getSymbol(value.ID))
        else:
            print(f"Symbol {value.ID} not declared")
            self.isAccepted = False
            return None

    @_('"(" expr ")"')
    def expr(self, value):
        return value.expr

    @_('"-" NUMBER %prec UMINUS')
    def expr(self, value):
        return -value.NUMBER

    @_('INT')
    def type(self, value):
        self.dataType = DataType.INT.name

    @_('DOUBLE')
    def type(self, value):
        self.dataType = DataType.DOUBLE.name

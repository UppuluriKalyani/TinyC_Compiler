import argparse
from sly import Parser
from Ast import *
from Function import *
from Program import *
from SymbolTable import *
from Lexer import TinyCLexer

class TinyCParser(Parser):
    tokens = TinyCLexer.tokens
    literals = TinyCLexer.literals
    stable = SymbolTable()

    @_('return_type ID "(" ")" "{" statements "}"')
    def program(self, value):
        prog = Program()
        fun = Function(value.return_type, value.ID)
        fun.setStatementsAstList(value.statements)
        fun.setLocalSymbolTable(self.stable.table)
        prog.addFunctionDetails(value.ID, fun)
        if prog.getMainFunction() is None:
            print("Error: main function is not defined")
        return prog

    @_('INT')
    def return_type(self, value):
        return value[0]

    @_('statement ";" statements')
    def statements(self, value):
        return [value[0]] + value[2]

    @_('statement ";"')
    def statements(self, value):
        return [value[0]]

    @_('declaration_stmt', 'assignment_stmt', 'print_stmt')
    def statement(self, value):
        return value[0]

    @_('type list_of_variables')
    def declaration_stmt(self, value):
        for val in value[1]:
            if not self.stable.nameInSymbolTable(val.symbolEntry):
                entry = SymbolTableEntry(val.symbolEntry, value[0])
                self.stable.addSymbol(entry)
            else:
                print(f"Error: redeclaration of '{val.symbolEntry}'")

    @_('ID "," list_of_variables')
    def list_of_variables(self, value):
        return [NameAst(value[0])] + value[2]

    @_('ID')
    def list_of_variables(self, value):
        return [NameAst(value[0])]

    @_('ID "=" ID')
    def assignment_stmt(self, value):
        left_entry = self.stable.getSymbolEntry(value[0])
        left = NameAst(left_entry.name)
        right_entry = self.stable.getSymbolEntry(value[2])
        right = NameAst(right_entry.name)
        return AssignAst(left, right, 0)

    @_('ID "=" CONST')
    def assignment_stmt(self, value):
        left_entry = self.stable.getSymbolEntry(value[0])
        left = NameAst(left_entry.name)
        return AssignAst(left, NumberAst(value[2]), 0)

    @_('PRINT ID')
    def print_stmt(self, value):
        return PrintAst(NameAst(value[1]))

    @_('INT')
    def type(self, value):
        return DataType.INT

    @_('CONST')
    def assignment_stmt(self, value):
        return NumberAst(int(value[0]))

# Main script
if __name__ == "__main__":
    lexer = TinyCLexer()
    parser = TinyCParser()

    apr = argparse.ArgumentParser()
    apr.add_argument('filename', help='Source file to parse')
    apr.add_argument('-Ast', action='store_true', help='Print AST if specified')
    args = apr.parse_args()

    with open(args.filename) as f:
        source_code = f.read()

    if args.Ast:
        obj = parser.parse(lexer.tokenize(source_code))
        obj.print()
    else:
        print('Error: Additional argument required to print AST')

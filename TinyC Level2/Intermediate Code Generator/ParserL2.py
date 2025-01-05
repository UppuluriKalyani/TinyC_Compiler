from sly import Parser
from tinyclexlevel2 import tinyclexer
from SymbolTable import SymbolTable, SymbolTableEntry
from IntermediateCode import Quadruple, Variable, Constant, NewTemp
from Program import Program
from Function import Function

class tinycparser(Parser):
    tokens = tinyclexer.tokens
    literals = tinyclexer.literals

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/', '%'),
    )

    lst = []
    localsymboltable = SymbolTable()
    prog = Program()

    @_('return_type ID "(" ")" "{" statements "}"')
    def program(self, value):
        fun = Function(int, value.ID)
        fun.setIntermediateCodeList(value.statements)
        self.prog.addFunctionDetails(value.ID, fun)
        return True

    @_('INT')
    def return_type(self, value):
        pass

    @_('statement ";" statements')
    def statements(self, value):
        return value[2]

    @_('statement ";"')
    def statements(self, value):
        return value[0]

    @_('dec_st')
    def statement(self, value):
        pass

    @_('ass_st')
    def statement(self, value):
        self.lst.append(value[0])
        return self.lst

    @_('print_st')
    def statement(self, value):
        pass

    @_('type list_var')
    def dec_st(self, value):
        for i in value.list_var:
            obj = SymbolTableEntry(i, int)
            self.localsymboltable.addSymbol(obj)

    @_('ID "," list_var')
    def list_var(self, value):
        return [value.ID] + value.list_var

    @_('ID')
    def list_var(self, value):
        return [value.ID]

    @_('expr "+" expr')
    def expr(self, value):
        t = NewTemp(int if value[0].getDatatype() == int and value[2].getDatatype() == int else double)
        obj = Quadruple(value.expr0, value.expr1, t, '+')
        self.lst.append(obj)
        return obj

    @_('INTCONST')
    def expr(self, value):
        obj = Constant(value[0])
        return obj

    @_('ID "=" expr')
    def ass_st(self, value):
        t = Variable(self.localsymboltable.getSymbolInTable(value.ID))
        obj = Quadruple(value.expr, None, t, '=')
        return obj

from sly import Parser

from L1Lexer import lex

class parse(Parser):

    tokens =lex.tokens

    literals =lex.literals

    memory = {}

    var_list = []

    @_('return_type ID "(" ")" "{" statements "}" ')

    def program(self,value):

        pass

    @_('INT')

    def return_type(self,value):

        pass

    @_('statement ";" statements')

    def statements(self,value):

        pass

    @_('statement ";"')

    def statements(self,value):

        pass

    @_('declaration_stmt')

    def statement(self,value):

        pass

    @_('assignment_stmt')

    def statement(self,value):

        pass

    @_('print_stmt')

    def statement(self,value):

        pass

    @_('type list_of_variables')

    def declaration_stmt(self,value):

        pass

    @_('ID "," list_of_variables')

    def list_of_variables(self,value):

        pass

    @_('ID')

    def list_of_variables(self,value):

        if value[0] not in self.var_list:

            self.var_list.append(value[0])

    @_('ID "=" ID')

    def assignment_stmt(self,value):

        self.memory[value[0]] = self.memory[value[2]]

    @_('ID "=" CONST')

    def assignment_stmt(self,value):

        if value[0] not in self.var_list:

            self.var_list.append(value[0])

        self. memory[value[0]] = value[2]

    @_('PRINT ID')

    def print_stmt(self,value):

        return (self.memory[value[1]])

    @_('INT')

    def type(self,value):

        pass

    @_('CONST')

    def assignment_stmt(self,value):

        return True



lexer =lex()

parser = parse()

import argparse

apr=argparse.ArgumentParser()

apr.add_argument('filename')

args= apr.parse_args()

f=open(args.filename)

t=f.read()

try:

        parser.parse(lexer.tokenize(t))

        print("Accepted:the program follows the grammar rules")

except Exception as e:

        print("Not Accepted:the program is not follows the grammar rules")




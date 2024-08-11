from sly import Parser

from Lex_tokens import CalcLexer

class CalcParser(Parser):

        tokens=CalcLexer.tokens

        literal=CalcLexer.literals

        precedence=(('left',"+","-"),('left',"*","/"))

        @_('L NEWLINE expr')

        def L(self,value):

                print(value[2])

        @_('expr')

        def L(self,value):

                print(value[0])

        @_('expr "+" expr')

        def expr(self,value):

                return value[0]+value[2]

        @_('expr "-" expr')

        def expr(self,value):

                return value[0]-value[2]

        @_('expr "*" expr')

        def expr(self,value):

                return value[0]*value[2]

        @_('expr "/" expr')

        def expr(self,value):

                return value[0]/value[2]

        @_(' "(" expr ")" ')

        def expr(self,value):

                return value[1]

        @_('INTEGER')

        def expr(self,value):

                return value[0]

        @_('ID')

        def expr(self,value):

                value[0]=int(input("enter a number\n"))

                return value[0]

lexer=CalcLexer()

parser=CalcParser()

import argparse

apr=argparse.ArgumentParser()

apr.add_argument('filename')

args= apr.parse_args()

f=open(args.filename)

t=f.read()

try:

        x=parser.parse(lexer.tokenize(t))

        print(x)

except Exception as e:

        print("Not valid Expression")


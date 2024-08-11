from sly import Lexer

class CalcLexer(Lexer):

        literals={'+','-','*','/','(',')','|'}

        tokens={INTEGER,NEWLINE,ID}

        ignore=' '

        NEWLINE=r'\n'

        INTEGER=r'[0-9]+'

        ID=r'[a-zA-Z]+'

        def INTEGER(self,t):

                t.value=int(t.value)

                return t


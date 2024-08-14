from sly import Lexer

class lex(Lexer):

    literals = (";","=","\n","==","+","-","*","/","%","!",",","(",")","{","}","[","]","<",">",".")

    ignore = " \n"

    ignore_comment = r'\//.*'

    tokens = ("ID","INT","PRINT","CONST")

    CONST = r'[0-9]+'

    ID = r'[a-zA-Z_][a-zA-Z_0-9]*'

    ID ['print'] = PRINT

    ID ['int'] = INT




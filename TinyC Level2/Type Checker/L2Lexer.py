from sly import Lexer

class LexicalAnalyzer(Lexer):
    literals = {'(', ')', '{', '}', ';', ',', '=', '+', '-', '*', '/', '%', '<', '>'}
    tokens = {
        NUMBER, FLOAT, ID, INT, DOUBLE, PRINT, EQUAL, NOTEQUAL,
        GREATEREQUAL, LESSEQUAL, LOGICALAND, LOGICALOR
    }

    ignore = ' \t'

    # Token definitions
    FLOAT = r'[0-9]+\.[0-9]+'
    NUMBER = r'[0-9]+'
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    # Reserved keywords
    ID['int'] = INT
    ID['double'] = DOUBLE
    ID['print'] = PRINT

    GREATEREQUAL = r'>='
    LESSEQUAL = r'<='
    EQUAL = r'=='
    NOTEQUAL = r'!='
    LOGICALAND = r'&&'
    LOGICALOR = r'\|\|'

    ignore_comment = r'\#.*'

    def FLOAT(self, t):
        t.value = float(t.value)
        return t

    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print(f"Illegal character {t.value[0]} on line {self.lineno}")
        self.index += 1

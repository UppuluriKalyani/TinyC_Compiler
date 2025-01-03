from sly import Lexer

class tinyclexer(Lexer):
    tokens = {INT, DOUBLE, ID, INTCONST, PRINT, DOUBLECONST, GREATERTHANEQUALS, LESSTHANEQUALS, 
              EQUALS, NOTEQUALS, LOGAND, LOGOR}
    literals = {'+', '-', '/', '*', '%', '<', '>', ',', '=', '(', ')', '{', '}', ';'}
    ignore = ' \t'
    ignore_newline = r'\n+'
    ignore_comments = r'\#.*'

    # Tokens
    ID = r'[a-zA-Z_][0-9a-zA-Z_]*'
    INTCONST = r'\d+'
    DOUBLECONST = r'[0-9]+\.[0-9]+'
    GREATERTHANEQUALS = r'>='
    LESSTHANEQUALS = r'<='
    EQUALS = r'=='
    NOTEQUALS = r'!='
    LOGAND = r'&&'
    LOGOR = r'\|\|'

    # Keywords
    ID['int'] = INT
    ID['double'] = DOUBLE
    ID['print'] = PRINT

    # Handlers
    @_('\d+')
    def INTCONST(self, t):
        t.value = int(t.value)
        return t

    @_('[0-9]+\.[0-9]+')
    def DOUBLECONST(self, t):
        t.value = float(t.value)
        return t

    @_('\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

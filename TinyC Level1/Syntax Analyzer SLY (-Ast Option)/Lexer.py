from sly import Lexer

class TinyCLexer(Lexer):
    # List of literal characters
    literals = {";", "=", "&", "|", "(", ")", "{", "}", ",", "+", "-", "*", "/", "!"}

    # Ignored characters (whitespace and newlines)
    ignore = " \n\t"

    # Token list
    tokens = {"ID", "INT", "PRINT", "CONST"}

    # Token regex patterns
    CONST = r'[0-9]+'
    ID = r'[a-zA-Z][a-zA-Z_0-9]*'

    # Keywords
    ID['print'] = PRINT
    ID['int'] = INT

    # Handle CONST token
    def CONST(self, t):
        t.value = int(t.value)
        return t

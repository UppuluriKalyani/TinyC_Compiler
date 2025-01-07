from sly import Lexer, Parser

class MaxLexer(Lexer):
    tokens = {NUMBER}
    ignore = ' \t'

    NUMBER = r'\d+'

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

class MaxParser(Parser):
    tokens = MaxLexer.tokens

    precedence = (
        ('left', 'NUMBER'),
    )

    def __init__(self):
        self.max_value = None

    @_('NUMBER')
    def statement(self, p):
        if self.max_value is None or p.NUMBER > self.max_value:
            self.max_value = p.NUMBER

    def parse(self, text):
        super().parse(text)
        return self.max_value

# Example usage:
lexer = MaxLexer()
parser = MaxParser()

numbers = "10 5 20 15"
result = parser.parse(lexer.tokenize(numbers))
print("Maximum value:", result)

from sly import Lexer

class ExprConvertLexer(Lexer):
	# Set of token names.This is always required
	literals = {"+","-","*","(",")"}
	tokens = { INTEGER}
	# Set of characters need be ignored
	ignore = ' '
	# Regular expression rules for tokens
	INTEGER  = r'[0-9]+'
	def INTEGER(self, t):
		t.value = int(t.value)
		return t

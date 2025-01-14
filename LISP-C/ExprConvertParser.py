from sly import Parser
from ExprConvertLexer import ExprConvertLexer
from ExprAst import *

class ExprConvertParser(Parser):
	tokens = ExprConvertLexer.tokens
	litearals = ExprConvertLexer.literals
	
	# @_('lispexpr')
	# def program(self, value):
	# 	#print("accepted")
	# 	return value[0]

	@_('cexpr')
	def program(self, value):
		#print("accepted")
		return value[0]


	# @_('"(" "-" arg arg ")"')
	# def lispexpr(self,value):
	# 	#pass
	# 	return MinusExprAst(value[2],value[3])

	# @_('"(" "+" arg arg ")"')
	# def lispexpr(self,value):
	# 	#pass
	# 	return PlusExprAst(value[2],value[3])

	@_('"(" arg "+" arg ")"')
	def cexpr(self,value):
		#pass
		return PlusExprAst(value[1],value[3])

    

	# @_('"(" "*" arg arg ")"')
	# def lispexpr(self,value):
	# 	pass

	@_('INTEGER')
	def arg(self,value):
		#pass
		return NumberAst(value[0])

	# @_('lispexpr')
	# def arg(self,value):
	# 	#pass
	# 	return value[0]
	
	@_('cexpr')
	def arg(self,value):
		#pass
		return value[0]
	
	
lexer = ExprConvertLexer()
parser = ExprConvertParser()
expression ='''( 2 + (3 + 5)) '''
x = parser.parse(lexer.tokenize(expression))
x.print()
print(" ")

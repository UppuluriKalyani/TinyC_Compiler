from abc import *

class AST(metaclass=ABCMeta):
	@abstractmethod
	def print(self):
		pass

class NumberAst(AST):
	def __init__(self, number):
		self.value = number
	def print(self):
		print(self.value,end="")

class ExprAst(AST):
	def __init__(self,left,right):
		self.left_ast = left
		self.right_ast = right
	def print(self):
		pass

class PlusExprAst(ExprAst):
	def __init__(self,left,right):
		super().__init__(left,right)

	def print(self):
		#pass
		print("+",end="")
		self.left_ast.print()
		self.right_ast.print()

class MinusExprAst(ExprAst):
	def __init__(self,left,right):
		super().__init__(left,right)

	def print(self):
		#pass
		self.left_ast.print()
		print("-",end="")
		self.right_ast.print()

class MultiplyExprAst(ExprAst):
	def __init__(self,left,right):
		super().__init__(left,right)
		
	def print(self):
		pass

# a = NumberAst(2)
# b = NumberAst(3)
# c = PlusExprAst(a,b)
# d = NumberAst(6)
# e = PlusExprAst(c,d)
# e.print()

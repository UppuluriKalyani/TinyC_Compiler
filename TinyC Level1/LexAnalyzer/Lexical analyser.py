from sly import Lexer

import argparse

class LA(Lexer):

        literals={"=","{","}","(",")",",",";"}

        tokens={INTEGER,ID,INT,PRINT,ASSIGN}

        ignore=' \n'

        INTEGER=r'[0-9]+'

        ID=r'[a-zA-Z]+'

        ID['int']=INT

        ID['print']=PRINT

        ASSIGN=r'='

lexer=LA()

apr=argparse.ArgumentParser()

apr.add_argument('filename')

apr.add_argument('-tokens', action='store_true')

args=apr.parse_args()

f=open(args.filename)

r=f.read()

try:

        if args.tokens:

                for token in lexer.tokenize(r):

                        print(f'type={token.type},value={token.value}')



except Exception as e:

      print('Error : expecting one more  argument')


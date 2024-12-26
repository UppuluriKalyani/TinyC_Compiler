from L2Parser import Level2Parser
from L2Lexer import LexicalAnalyzer
from spim import generator
import argparse
import sys

if __name__ == "__main__":
    lexer = LexicalAnalyzer()
    parser = Level2Parser()
    arp = argparse.ArgumentParser()
    arp.usage = "tcc [options] file"
    arp.add_argument("file", help="input program file")
    arp.add_argument('-T', "--tokens", action='store_true', help="Saves the tokens in the input in .toks file")
    arp.add_argument('-P', "--parse", action='store_true', help="Parses the given input and print if it is accepted or not")
    arp.add_argument("-A", "--ast", action='store_true', help="Prints the AST of the given input file")
    arp.add_argument("-S", "--syb", action='store_true', help="Prints the Symbol table of the given input file")
    arp.add_argument("-C", "--compile", action='store_true', help="Compiles the given input file to filename.s")
    
    args = arp.parse_args()
    expression = ""
    
    with open(args.file, "r") as f:
        expression = f.read()
    
    args.compile = True
    
    if args.tokens:
        with open(f'{args.file}.toks', "w") as f:
            for token in lexer.tokenize(expression):
                f.write(f"Type: {token.type},\t\t\t\tvalue: {token.value}\t\t\t\tLine no: {token.lineno}\n")
    
    parse = parser.parse(lexer.tokenize(expression))
    
    if args.parse:
        if parse:
            print("Program Accepted")
        else:
            print("Program Not Accepted")
        args.compile = False
        args.ast = False
    
    if args.syb:
        parser.localSymbolTable.printSymbolTable()
    
    originalStdout = sys.stdout
    
    if args.ast:
        with open(f'{args.file}.ast', 'w') as f:
            sys.stdout = f
            parser.program.print()
        sys.stdout = originalStdout
        print("AST file Generated")
    
    if args.compile:
        with open(f'{args.file}.s', 'w') as f:
            sys.stdout = f
            generator(parser)
        sys.stdout = originalStdout
        print(f"File compiled to {args.file}.s")

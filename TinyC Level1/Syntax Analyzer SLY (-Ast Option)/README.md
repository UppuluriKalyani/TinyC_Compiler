## Aim: To implement Syntax Analyzer which constructs syntax tree for level 1 of TinyC using SLY.
### Description:
Constructs a syntax tree (AST) for Level 1 of TinyC using SLY:
### 1.Define Grammar:
Specify the grammar for TinyC Level 1 to describe the valid syntax.
### 2.Create Lexer:
Develop a lexer to tokenize the source code.
### 3.Create Parser:
Use SLY to define parsing rules based on the grammar and construct the syntax tree while parsing.
### 4. AST Nodes:
Define data structures or classes to represent nodes in the syntax tree.
### 5.AST Construction:
Build the syntax tree by creating nodes for recognized language constructs during parsing.
### 6. Error Handling:
Implement error detection and recovery mechanisms for syntax errors without disrupting tree construction.
### 7.Testing:
Thoroughly test the parser and AST construction with various TinyC Level 1 programs.
### 8. AST Traversal:
Prepare for subsequent phases by enabling tree traversal.
### 9. Integration:
Ensure smooth integration with other compiler phases if needed.
### 10. Option Handling:
Implement options to control whether the syntax tree should be constructed.
## Eamples
**Example1**:

int main(){

int a;

a=30;

print a;

}

**Output**:

![image](https://github.com/user-attachments/assets/a80f7cbc-3e98-40f8-ab3c-9a90d4ca2f6b)


**Example2**:

int main(){

int a,b,c;

a=30;

b=40;

c=20;

print a;

print b;

print c;

}

**Output**:

![image](https://github.com/user-attachments/assets/d1d8c083-46f7-4b4c-a8ba-d06a16a9a68c)

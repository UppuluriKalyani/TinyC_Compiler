## Implement a Type Checker for Level 2 of TinyC using SLY.


---

### Description

#### 1. Parser Definition

Utilize SLY (Sly Lex-Yacc) to construct a parser for Level 2 TinyC.

Define grammar rules for handling statements, expressions, and declarations in the TinyC programming language.



---

#### 2. Symbol Table

Develop a Symbol Table to track variables and their associated data types.

Ensure consistency and validity across variable usage in the program.



---

#### 3. Type Checking Rules

Define type checking rules based on the specifications of Level 2 TinyC, including:

Arithmetic Operations: Ensure data type compatibility.

Relational and Logical Expressions: Validate type consistency.

Variable Usage: Enforce correct and consistent usage of variables.




---

#### 4. Integration with Parsing

Seamlessly integrate the type checking mechanism into the parsing process.

Perform type validation during parsing for all statements and expressions.

Update the Symbol Table dynamically as new variables and types are declared or updated.



---

#### 5. Error Handling

Implement robust error handling for type-related issues.

Detect and report issues such as:

Type Mismatches in assignments or operations.

Undeclared Variable Usage or re-declarations.

Invalid Operations between incompatible types.


Provide clear and meaningful error messages to help programmers debug and resolve issues effectively.



---

### Tools and Technologies

Python

SLY (Sly Lex-Yacc for Python)


# TinyC Compiler - Level 2

## Overview

Level 2 of the TinyC Compiler expands on the basic functionality provided in Level 1, introducing additional data types, operators, and expressions. This level builds on the foundation of Level 1, allowing for more complex programs and deeper understanding of compiler components.

## Grammar and Features

### Program Structure

- **Single Function**: Similar to Level 1, the program consists of only one function, `main()`.

### Keywords

- **Supported Keywords**: `int`, `print`, `double`.

### Data Types

- **Supported Data Types**: `int`, `double`.

### Identifiers

- **Naming Rules**: Identifiers must start with a letter (uppercase or lowercase) and can be followed by one or more digits or underscores.

### Statements

- **Allowed Statements**:
  1. **Declaration Statement**: Used to declare variables (e.g., `int a;`, `double b;`).
  2. **Assignment Statement**: Used to assign values to variables (e.g., `a = 30;`, `b = 45.6;`).
  3. **Print Statement**: Used to output the value of a variable (e.g., `print a;`).

### Print Statement Syntax

- **Syntax**: The `print` statement follows the format `print identifier`, where `identifier` is the variable to be printed.

### Expressions

Level 2 introduces more complex expressions, allowing for a broader range of operations:

1. **Arithmetic Operators**: `+`, `-`, `*`, `/`, `%`.
2. **Type Casting**: Allows explicit type conversion (e.g., `(int) b`).
3. **Relational Operators**: `<`, `>`, `<=`, `>=`, `==`, `!=`.
4. **Logical Operators**: `&&`, `||`.

## Implementation Details

### Lexical Analyzer

The lexical analyzer identifies keywords, operators, identifiers, and other tokens, supporting the expanded grammar of Level 2 TinyC.

### Syntax Analyzer

The syntax analyzer parses tokens and builds a syntax tree that represents the structure of the TinyC program. This tree is used in subsequent stages of compilation, including type checking and code generation.

### Type Checker

The type checker ensures that operations within the program are semantically correct, particularly focusing on the compatibility of different data types (e.g., `int` and `double`).

### Intermediate Code Generation

The compiler generates intermediate code from the syntax tree, which is then optimized before generating the final target code.

### Target Code Generation

Finally, the optimized intermediate code is translated into assembly code, which can be executed by the SPIM simulator or another appropriate assembly language environment.

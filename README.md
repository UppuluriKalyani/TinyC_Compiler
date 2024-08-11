# TinyC Compiler

This repository contains a compiler for the TinyC programming language, designed to convert TinyC source code into assembly language. The compiler is implemented in Python using the SLY library and supports two levels of functionality, each with its own set of features.

## Features

- **Level 1**:
  - Basic TinyC grammar with limited keywords and data types.
  - Supports integer data type and simple statements.
  - Constructs a syntax tree during syntax analysis.

- **Level 2**:
  - Extended TinyC grammar with additional keywords, data types, and expressions.
  - Includes type checking, intermediate code generation, and target code generation.
  - Supports both integer and double data types, along with more complex expressions and control structures.

## Project Structure

- **Level1/**: Contains the implementation details, examples, and tests for Level 1 of TinyC.
- **Level2/**: Contains the implementation details, examples, and tests for Level 2 of TinyC.

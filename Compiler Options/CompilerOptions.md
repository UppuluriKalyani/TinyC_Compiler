## Study of Compiler Options

### Aim
To understand and explore various compiler options that influence the behavior, performance, and debugging of the compiled code.

## Description

- Compiler options are settings and commands used during the compilation process to:

- Control aspects like optimization, warnings, and linking.

- Influence the behavior and performance of the resulting program.


## Common Compiler Options

- 1. -O2 or -O3 (Optimization Levels)

Improve program performance through code optimization.

-O2: Moderate optimization.

-O3: High-level optimization for maximum performance.


- 2. -Wall (Enable Warnings)

Enables most compiler warning messages.

Helps in identifying potential issues during code development.


- 3. -I (Include Paths)

Specifies additional directories for header files.

Useful for including custom or third-party libraries.


- 4. -L (Library Paths) and -l (Libraries)

-L: Adds search paths for libraries.

-l: Links specific libraries to the program.


- 5. -std (Language Version)

Specifies the language standard to follow (e.g., -std=c99, -std=c++11).

Ensures compatibility with specific versions of the language.


- 6. -g (Debug Information)

Includes debugging symbols in the compiled program.

Allows easier debugging with tools like gdb.


- 7. -Werror (Treat Warnings as Errors)

Treats all warnings as errors.

Prevents compilation if warnings are detected.


## GCC Compiler Options

- 1. -E Option (Preprocessing)

**Performs preprocessing tasks like:**

Macro expansion.

Header file inclusion.

Conditional compilation.


Outputs preprocessed code to the standard output.


- 2. -S Option (Generate Assembly)

Generates human-readable assembly code with .s extension.

Allows inspection of the assembly code for optimization purposes.

Does not produce executable files.


- 3. -O Option (Optimization)

Optimizes code for better performance or smaller size.

Levels include:

-O0: No optimization.

-O1: Basic optimizations.

-O2: Moderate optimizations.

-O3: High-level optimizations.



- 4. -c Option (Compile Only)

Compiles source code into object files without linking.

Useful for modular compilation by creating intermediate object files.


### Usage Example

gcc -Wall -O2 -Iinclude_path -Llib_path -lmylib -o output_file source_file.c

Explanation

- 1. -Wall: Enables warning messages.


- 2. -O2: Applies moderate optimization.


- 3. -I & -L: Adds include and library paths.


- 4. -lmylib: Links the specified library.


- 5. -o output_file: Specifies the output executable name.



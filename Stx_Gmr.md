# Language Specification for Python Extension with Repeat Functionality

## Overview
This extension to Python allows users to repeat print statements and method calls using the `*` operator followed by a numeric value, indicating the number of repetitions.

## Syntax

### Print Statement Extension
- Format: `print(expression) * n`
- Description: Prints the output of `expression` n times.
- Example: `print("Hello World") * 3` would print "Hello World" three times.

### Method Call Extension
- Format: `object.method(args) * n`
- Description: Calls `method` on `object` with `args` n times.
- Example: `my_object.greet() * 2` would call the `greet` method on `my_object` two times.

## Grammar

- `statement -> print_statement | method_call`
- `print_statement -> 'print' '(' expression ')' '*' NUMBER`
- `method_call -> IDENTIFIER '.' IDENTIFIER '(' optargs ')' '*' NUMBER`
- `expression -> STRING | NUMBER | expression OP expression`
- `optargs -> expression | expression ',' optargs`
- `IDENTIFIER -> [a-zA-Z_][a-zA-Z0-9_]*`
- `NUMBER -> [0-9]+`
- `STRING -> '".*"' | "'.*'"`

## Notes
- This grammar is built on top of the existing Python grammar and only describes additions or modifications.

# 🚀 Python Extension: Repeat Functionality Specification

## 🌐 Overview
This extension enhances Python by allowing the repetition of print statements and method calls using the `*` operator followed by a numeric value, indicating the number of repetitions. It's designed to simplify repetitive tasks in coding by streamlining multiple executions.

## 📝 Syntax Specifications

### 1️⃣ Print Statement Extension
- **Format:** `print(expression) * n`
- **Description:** Outputs the result of `expression` n times.
- **Example:** `print("Hello World") * 3` — This will output "Hello World" three times.

### 2️⃣ Method Call Extension
- **Format:** `object.method(args) * n`
- **Description:** Executes `method` on `object` with provided `args` n times.
- **Example:** `my_object.greet() * 2` — This calls the `greet` method on `my_object` twice.

## 📘 Grammar Definitions

- **Statement:**  
  📃 `statement -> print_statement | method_call`

- **Print Statement:**  
  🖨️ `print_statement -> 'print' '(' expression ')' '*' NUMBER`

- **Method Call:**  
  📞 `method_call -> IDENTIFIER '.' IDENTIFIER '(' optargs ')' '*' NUMBER`

- **Expression:**  
  🧮 `expression -> STRING | NUMBER | expression OP expression`

- **Optional Arguments:**  
  📌 `optargs -> expression | expression ',' optargs`

- **Identifier:**  
  🔤 `IDENTIFIER -> [a-zA-Z_][a-zA-Z0-9_]*`

- **Number:**  
  🔢 `NUMBER -> [0-9]+`

- **String:**  
  📜 `STRING -> '".*"' | "'.*'"`

## 📄 Additional Notes
- 🛠 This grammar is built on top of the existing Python grammar and only describes additions or modifications to facilitate repeated executions seamlessly.


import sys
import re

def preprocess(code):
    """Preprocess the custom syntax to replace function and method calls followed by a multiplier with a loop."""
    # Enhanced regex to handle more general function and method calls, including nested ones
    pattern = re.compile(r'(\w+\([^\)]*\)|\w+\.\w+\([^\)]*\))\s*\*\s*(\d+)')

    # Function to replace matched pattern with a loop structure
    def repl(match):
        statement, times = match.group(1), int(match.group(2))
        return 'for _ in range({}): {}'.format(times, statement)

    # Apply replacement function to the code
    code = pattern.sub(repl, code)
    return code

def execute(code):
    """Execute the Python code after preprocessing."""
    local_globals = {}
    try:
        # Execute the preprocessed code
        exec(preprocess(code), local_globals, local_globals)
    except Exception as e:
        print(f"Execution failed with error: {e}")
        sys.exit(1)

def main():
    """Main function to handle command-line execution."""
    if len(sys.argv) != 2:
        print("Usage: pyextend <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            code = file.read()
        execute(code)
        print("Execution successful.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

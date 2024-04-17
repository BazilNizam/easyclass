import sys
import re

def preprocess(code):
    """Preprocess the custom syntax to replace function and method calls followed by a multiplier with a loop."""
    # Generalize the pattern to match function calls or method calls
    pattern = re.compile(r'(\w+\([^\)]*\)|\w+\.\w+\([^\)]*\))\s*\*\s*(\d+)')
    while True:
        match = pattern.search(code)
        if not match:
            break
        full_match, statement, times = match.group(0), match.group(1), int(match.group(2))
        # Create a for loop to repeat the statement the specified number of times
        replacement = 'for _ in range({}): {}'.format(times, statement)
        code = code.replace(full_match, replacement)
    return code

def execute(code):
    """Execute the Python code after preprocessing."""
    local_globals = {}
    exec(preprocess(code), local_globals, local_globals)

def main():
    """Main function to handle command-line execution."""
    if len(sys.argv) != 2:
        print("Usage: easy <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        code = file.read()
    execute(code)

if __name__ == '__main__':
    main()

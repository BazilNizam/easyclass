import re

def preprocess(code):
    pattern = re.compile(r'(print\(.*?\)|\w+\.\w+\(.*?\))\s*\*\s*(\d+)')
    while True:
        match = pattern.search(code)
        if not match:
            break
        full_match = match.group(0)
        statement = match.group(1)
        times = int(match.group(2))
        replacement = 'for _ in range({}): {}'.format(times, statement)
        code = code.replace(full_match, replacement)
    return code

def execute(code):
    local_globals = {}
    exec(preprocess(code), local_globals, local_globals)

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m pyextend 'code'")
        sys.exit(1)
    code = sys.argv[1]
    execute(code)

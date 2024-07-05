import sys
import re

def get_result(lines):
    s = "\n".join(lines)
    
    # Remove comments
    s = re.sub(r'-.*$', '', s, flags=re.MULTILINE)
    
    statements = []
    current = ""
    in_string = False
    quote_char = ""
    
    i = 0
    while i < len(s):
        char = s[i]
        
        if in_string:
            if char == quote_char and (i == 0 or s[i - 1] != '\\'):
                in_string = False
            current += char
        else:
            if char == '"' or char == "'":
                in_string = True
                quote_char = char
                current += char
            elif char == ';':
                if current.strip():
                    statements.append(current.strip())
                current = ""
            else:
                current += char
        i += 1
    
    if current.strip():
        statements.append(current.strip())
    
    return len(statements)

def main():
    lines = []
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            print(get_result(lines))
            lines.clear()
        else:
            lines.append(line)

if __name__ == "__main__":
    main()

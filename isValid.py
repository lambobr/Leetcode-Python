"""This function checks if a string containing only parenthesis, brace and bracket is valid"""

def isValid(s: str) -> bool:
    stack=[]
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        elif stack[-1]=='(' and s[i]==')' or stack[-1]=='[' and s[i]==']' or stack[-1]=='{' and s[i]=='}':
            stack.pop()
        else:
            stack.append(s[i])
    if not stack:
        return True
    return False
        

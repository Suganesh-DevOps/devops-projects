def removeDuplicates(s: str) -> str:
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Remove the duplicate
        else:
            stack.append(char)  # Add non-duplicate
    
    return ''.join(stack)

print(removeDuplicates('abbccd'))

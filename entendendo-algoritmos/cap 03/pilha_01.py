stack = [1, 2, 3, 4, 5]

def push(elemento):
    stack.append(elemento)

def pop():
    if not is_empty():
        return stack.pop(-1)
    return None

def peek():
    if not stack():
        return stack[-1]
    return None

def is_empty():
    return len(stack) == 0

def size():
    return len(stack)

print(stack)
push(6)
print(stack)
pop()
print(stack)
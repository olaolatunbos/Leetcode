tokens = ["1", "2", "+"]
stack = []
for i in tokens:
    if i != "+":
        stack.append(i)
    elif i == "+":
        while stack:
            li = []
            for i in range(2):
        stack.append(added)
print(stack)

temperatures = [73,74,75,69,71,72]

stack = []
output = []
for i, t in enumerate(temperatures):
    if stack:
        while stack:
            if t > stack[-1][1]:
                output.append([i - stack[-1][0]])
                stack.pop()
    else:
        stack.append([i, t])
print(output)
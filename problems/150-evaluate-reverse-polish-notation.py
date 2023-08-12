class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a+b)
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == "*":
                a, b = stack.pop(), stack.pop()
                res = a*b
                stack.append(res)
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        
        return stack[0]
            

            

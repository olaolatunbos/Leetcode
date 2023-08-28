def myAtoi(s):
        new = ""
        for c in s:
            if c.isdigit or c == "-":
                new += c

        return new

print(myAtoi("wit words 123"))
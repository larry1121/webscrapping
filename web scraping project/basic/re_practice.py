import re

p=re.compile("ca.e")

def print_match(m):
    if m:
        print(m.group())
    else:
        print("not match")

print(p)
print_match(p)
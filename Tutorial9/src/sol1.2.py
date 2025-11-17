word = input().split()[-1]
result = ""
for char in word:
    if char.isalpha():
        result += char
print(result)

# Hello World.
# This item sells for ten HKD.
# This is an example

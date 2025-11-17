strings = input().split(',')
result = int(strings[0])
for string in strings:
    number = int(string)
    if number > result:
        result = number
print(result)

# 123,456,879,100
# 1,2,3,45,678,50,-4
# 8,9,10,4,8

def count_up_to(limit: int):
    count = 1
    while count <= limit:
        yield count
        count += 1
    return 

print(list(count_up_to(5)))
# Output: [1, 2, 3, 4, 5]
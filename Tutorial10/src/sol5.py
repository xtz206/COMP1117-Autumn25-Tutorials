def main():
    max_length = 0
    current_length = 0
    previous_number = None
    while True:
        current_number = int(input())
        if current_number == 0:
            break
        if current_number == previous_number:
            current_length += 1
        else:
            current_length = 1
            previous_number = current_number
        if current_length > max_length:
            max_length = current_length

    print(max_length)


if __name__ == "__main__":
    main()

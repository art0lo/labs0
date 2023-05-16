def square_digits(num):
    result = ""
    for digit in str(num):
        square = int(digit) ** 2
        result += str(square)
    return int(result)


# Example usage
print(square_digits(9119))  # Output: 811181
print(square_digits(765))   # Output: 493625

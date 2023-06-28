def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary != 0:
        decimal += (binary % 10) * (2 ** power)
        binary //= 10
        power += 1
    return decimal


def decimal_to_binary(decimal):
    binary = 0
    power = 0
    while decimal != 0:
        binary += (decimal % 2) * (10 ** power)
        decimal //= 2
        power += 1
    return binary


# Test the functions
binary_number = input("Enter a binary number: ")
decimal_number = int(input("Enter a decimal number: "))

decimal_result = binary_to_decimal(int(binary_number))
binary_result = decimal_to_binary(decimal_number)

print("Decimal equivalent of", binary_number, "is", decimal_result)
print("Binary equivalent of", decimal_number, "is", binary_result)

def sum_of_squares(numbers):
    total = 0

    for num in numbers:
        total += num ** 2

    return total

numbers = [1, 2, 3, 4, 5]

print("Sum of Squares:", sum_of_squares(numbers))
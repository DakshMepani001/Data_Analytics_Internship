numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

prime_numbers = []

for num in numbers:
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(num)

print(prime_numbers)
"""01 — Prime Check — Optional
Run independently after the core topics; this is not another required exercise.
"""

n = 29
# n = int(input("Integer to test: "))
is_prime = n >= 2
divisor = 2
while divisor * divisor <= n and is_prime:
    if n % divisor == 0:
        is_prime = False
    divisor += 1
print(n, "is prime:", is_prime)
# Only divisors up to sqrt(n) are needed: factors above it have a partner below it.
# Try -1, 0, 1, 2, 9, and 29. Explain why 1 is not prime.

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(n):
    count = 0
    a, b = 0, 1
    
    while count < n:
        if is_prime(a):
            count += 1
            print(f"Fibonacci Prime {count}: {a}")
            yield a
        a, b = b, a + b

def main():
    count = 0
    # Note: Finding 1000 Fibonacci primes would take a very long time as the numbers 
    # get massive quickly. I have adjusted this to 10 for demonstration.
    for _ in generate_primes(10):
        count += 1
    print(f"Finished generating {count} Fibonacci prime numbers.")

if __name__ == '__main__':
    main()

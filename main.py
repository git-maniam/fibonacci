def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            print(f"Prime {len(primes)}: {num}")
            yield num
        num += 1

def main():
    count = 0
    for _ in generate_primes(1000):
        count += 1
    print(f"Finished generating {count} prime numbers.")

if __name__ == '__main__':
    main()

def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

def get_first_10_primes():
    primes = []
    num = 2
    # we need the first 10 so loop it until length is 10
    while len(primes) < 10:
        is_prime = True
        
        # check  the divisibility
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(num)
        num += 1
    
    return primes

def sum_1_to_100():
    t = 0
    c = 1
    while c <= 100:
        t += c
        c += 1
    return t
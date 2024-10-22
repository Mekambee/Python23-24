import sys
def factorize(number):
    i = 2
    factors = []
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors

def format_output(factors):
    if not factors:
        return ""

    factor_counts = {}

    for factor in factors:
        if factor in factor_counts:
            factor_counts[factor] += 1
        else:
            factor_counts[factor] = 1

    formatted = []
    for factor, count in factor_counts.items():
        if count > 1:
            formatted.append(f"{factor}^{count}")
        else:
            formatted.append(f"{factor}")

    return "*".join(formatted)

if __name__ == "__main__":
    argv = sys.argv[1:]
    numbers = []
    for i in range(0, len(argv)):
        number = int(argv[i])
        numbers.append(number)

    for number in numbers:
        factors = factorize(number)
        formatted_output = format_output(factors)
        print(f"{number} = {formatted_output}")

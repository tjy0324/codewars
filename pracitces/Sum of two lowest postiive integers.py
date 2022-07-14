# At first, I tried below

def sum_two_smallest_numbers(numbers):
    low = min(numbers)
    numbers.pop(numbers.index(low))
    second_low = min(numbers)
    return low + second_low

# However, below is much better


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

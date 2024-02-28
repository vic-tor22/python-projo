def fibonacci_sequence(limit):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

fib_sequence = fibonacci_sequence(100)
print(fib_sequence)

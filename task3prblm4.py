def fibonacci_sequence(n):
    x = [1, 2]
    while x[-1] + x[-2] <= n:
        x.append(x[-1] + x[-2])
    return x

def even_sum(sequence):
    return sum(filter(lambda x: x % 2 == 0, sequence))

def main():
        N = int(input("Enter the upper limit for Fibonacci Sum: "))
        sequence = fibonacci_sequence(N)
        even_numbers = list(filter(lambda x: x % 2 == 0, sequence))
        result = even_sum(sequence)
        print(f" Even Fibonacci numbers up to {N}: {even_numbers}. Their sum is {result}.")

if _name_ == "_main_":
    main()

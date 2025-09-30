def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

try:
    # Get user input for the number of Fibonacci numbers
    num = int(input("Enter how many Fibonacci numbers you want (positive integer): "))
    if num < 0:
        raise ValueError("Please enter a positive number.")
    
    # Generate and print the sequence
    fib_sequence = fibonacci(num)
    print("\nFibonacci Sequence:")
    for i, value in enumerate(fib_sequence, 1):
        print(f"Number {i}: {value}")

    # Calculate and display the sum of the sequence
    sequence_sum = sum(fib_sequence)
    print(f"\nSum of the sequence: {sequence_sum}")

except ValueError as e:
    print(f"Error: {e}. Please enter a valid positive integer.")

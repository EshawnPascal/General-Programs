# Solution to the Fibonacci Sequence
n = int(input("Enter the nth term of the Fibonacci Sequence to find: "))

def fib(n):
    """Define the Fibonacci Sequence and its solution"""
    fib_numbers = []
    a, b = 0, 1
    fib_numbers.append(a)
    for i in range(1, n):
        a, b = b, a+b
        fib_numbers.append(a)
        continue
    
    # Print the results of the Fibonacci sequence to the nth term and display the results
    print("The " + str(n) + "th term of the sequence is " + str(fib_numbers[-1]))
    print("All terms up to the nth term: "+ str(fib_numbers))

fib_function = fib(n)
        
    

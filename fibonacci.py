# fibonacci.py
# This program generates the Fibonacci sequence up to n terms.

def fibonacci(n):
    """Prints the Fibonacci sequence up to n terms."""
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Example usage
if __name__ == "__main__":
    terms = int(input("Enter the number of terms: "))
    fibonacci(terms)

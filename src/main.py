import time
import random


"""
LINEAR TIME COMPLEXITY: O(n)
----------------------------
Definition:
An algorithm is said to have linear time complexity when the time it takes 
to complete its execution is directly proportional to the size of the input (n).

Mathematical Notation: O(n)
- 'O' represents Big O Notation (the upper bound of growth).
- 'n' represents the number of elements in the input.

Key Characteristics:
1. Growth: If you double the input size, the time taken roughly doubles.
2. Iteration: Usually involves a single loop that visits every element once.
3. Scalability: Much more efficient than O(n²) (Quadratic), but slower than 
   O(log n) (Logarithmic) or O(1) (Constant).
"""


def find_max_linear(data_list):
    """
    EXPLANATION:
    This function finds the maximum value in a list
    To do this, it MUST look at every single element exactly one

    If the list has 10 items, the loop runs 10 times
    If the list has 1,000,000 items, the loop runs 1,000,000 times.
    This is definition of O(n)
    """

    # Check if the list is empty (Constant time check)
    if not data_list:
        return None
    

    # Initialize the maximum with the first elemnet
    current_max = data_list[0]

    # Start with linear san (The O(n) part)
    # We iterate through "n" elements
    for item in data_list:
        if item > current_max:
            current_max = item

    return current_max







def run_demonstration():
    """
    Demonstrates the linear growth by timing the function with
    different input sizez
    """

    # Test cases: Small size vs Large size
    sizes = [10000, 1000000, 50000000]

    print(f"{"Input Size (n)":<20} | {"Time Taken (seconds)":<20}")
    print("-" * 45)

    for n in sizes:
        # Generate a random list of size n
        test_data = [random.randint(0,1000000) for _ in range(n)]

        # Record the start time
        start_time = time.time()

        # Execute end time
        find_max_linear(test_data)

        # Record end time
        end_time = time.time()

        elasped = end_time - start_time
        print(f"{n:<20,} | {elasped:<20.6f}")









if __name__ == "__main__":
    # Title and Introduction
    print("Python Algorithm Analysis: O(n) Linear Time\n")
    
    # Run the timing demo
    run_demonstration()
    
    print("\nOBSERVATION:")
    print("Notice how the time taken grows at roughly the same rate as the input size.")
    print("If n is 5x larger, the execution time is roughly 5x longer.")

"""
REAL-WORLD EXAMPLES OF O(n):
- Reading a book (you read every page once).
- Searching for a specific card in an unsorted deck.
- Counting the number of people in a line.
- Summing all numbers in an array.
"""
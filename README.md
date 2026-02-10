# Linear-Time

**Explanation of Linear Time Complexity (O(n))**

This repository provides examples and explanations related to **linear time complexity** — a type of algorithmic complexity where the execution time grows in direct proportion to the size of the input.

---

## 📊 What Is Linear Time (O(n))?

In algorithm analysis, **linear time complexity**, written as **O(n)**, means that an algorithm’s running time increases *linearly* with the size of the input. In other words, if the input size doubles, the number of steps the algorithm performs also roughly doubles.

This is one of the most common time complexities in computer science and typically occurs when an algorithm needs to **examine every element in the input once**.

---



## 📌 Common Examples of O(n) Algorithms

Here are typical situations where time complexity is linear:

- **Linear Search:** Check every element in a list until the target is found.
- **Finding Maximum/Minimum:** Scan all elements to find the largest or smallest value.
- **Iterating or Printing All Elements:** Visiting each element in a list once.

---

## 📁 Source Code
```python
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
```


---
## 🧠 Why Linear Time Matters

Linear time complexity is efficient and often **the best possible time** in cases where you *must* look at every element in a dataset (e.g., searching or scanning all values). Since the running time grows proportionally with input size, algorithms with O(n) complexity remain manageable for larger inputs. :contentReference[oaicite:3]{index=3}


# Dynamic Programming

## Dynamic Programming Defined
> Dynamic programming amounts to **bracking down an optimiztion problem** into simpler sub-problems, and **storing the solution to each sub-problem** so that each sub-problem is only solved once.

## Example Memoization with Fibonacci Numbers

Recursive algorithm pattern of Fibonacci Number, which write in Python will be like:
```python
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

import time
start = time.time()
result = fib(5)
end = time.time()
print(end - start)
```
this will repeated the computation like you `n = 3` will reslove thrice. We need think about a way to avoid this repeated computation, what if we make a array to store the `fib` value have been computed, that is what the memoization does.
```python
def fib_memo(n):
    # create a array to store the computed fib value
    memo = [0] * (n + 1)
    memo[0], memo[1]=0, 1
    for i in range(2, n + 1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

fib_memo(100)
```
The memo array is iteratively filled in by the loop staring from fib(2), when calculated the fib(3), it will use the fib value memo(2) and memo(1) which are stored before. And you can notice the time for execution have been reduced significantly. For the space complexity, this solution will cost $O(n)$ as we open a 1-dim array to store the data.

# Design the Dynamic Programming Process

* Step 1: Identify the sub problem in words.

Use you words to describe the sub-problem that you have identified within the original problem.

* Step 2: Write out the sub-problem as a recurring mathematical decision.

Well, the mathematical recurrence, or repeated decision, that you find will eventually be what you put into your code. 

* Step 3: Solve the original problem using Steps 1 and 2.

* Step 4: Determine the dimensions of the memoization array and the direction in which it should be filled.

# Runtime Analysis of Dynamic Programs

Now for the fun part of writing algorithms: runtime analysis. I’ll be using big-O notation throughout this discussion . If you’re not yet familiar with big-O, I suggest you read up on it here.

Generally, a dynamic program’s runtime is composed of the following features:

* Pre-processing
* How many times the for loop runs
* How much time it takes the recurrence to run in one for loop iteration
* Post-processing

Overall, runtime takes the following form:
```
Pre-processing + Loop * Recurrence + Post-processing
```
Let’s perform a runtime analysis of the punchcard problem to get familiar with big-O for dynamic programs. Here is the punchcard problem dynamic program:
```python
def punchcardSchedule(n, values, next):
 # Initialize memoization array - Step 4
  memo = [0] * (n+1)
  
 # Set base case
  memo[n] = values[n]
  
 # Build memoization table from n to 1 - Step 2
  for i in range(n-1, 0, -1):
    memo[i] = max(v_i + memo[next[i]], memo[i+1])
 
 # Return solution to original problem OPT(1) - Step 3
  return memo[1]
```

Let’s break down its runtime:

* Pre-processing: Here, this means building the the memoization array. O(n).
* How many times the for loop runs: O(n).
* How much time it takes the recurrence to run in one for loop iteration: The recurrence takes constant time to run because it makes a decision between two options in each iteration. O(1).
* Post-processing: None here! O(1).
The overall runtime of the punchcard problem dynamic program is O(n) O(n) * O(1) + O(1), or, in simplified form, O(n).

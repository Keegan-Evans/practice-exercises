# threeRecursionProblems.py
# My preliminary answers to the problems posed in:
# https://www.youtube.com/watch?v=ngCos392W4w&ab_channel=Reducible
# before watching his answers.
"""
1. What is the simplest possible input?
2. Play around with visualizations and examples
3. Relate hard cases to simpler cases.
4. Generalize the pattern.
5. Write code by combining the pattern with the base case.
"""
# Problem 1 
# Write a recursive function that given n, sums all non-negative integers
# up to n.

def recSum(n):
    def recSumHelper(x, soFar):
        if x == n:
            return soFar + x
        else:
            return recSumHelper(x + 1, soFar + x)

    return recSumHelper(0, 0)

def recSum2(n):
    if n == 0:
        return 0
    else:
        return n + recSum2(n - 1)

# Problem 2
# Write a function that takes two inputs n and m, and outputs the number of
# unique paths from the top left corner to the bottom right corner of a n*m
# grid. You can only move down or right 1 unit at a time.

# Problem 3

if __name__ == '__main__':
    a = recSum(387)
    print(a)

    b = recSum2(5)
    print(b)

def find_max(nums):
    if not nums:
        raise ValueError("Array must not be empty")

    best = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > best:
            best = nums[i]

    return best

print(find_max([1,2,3,4,5,6,7]))

# Problem: You are given an array prices, where prices[i] is the price of a stock on day i.
# Choose one day to buy and a later day to sell. Return the maximum profit. If no profit is possible, return 0.
#This is a classic array traversal problem because we can solve it by remembering useful information from the past.

#bruteforce
def max_profit_brute(prices):
    best = 0

    for buy in range(len(prices)):
        for sell in range(buy + 1, len(prices)):
            profit = prices[sell] - prices[buy]
            best = max(best, profit)

    return best

def max_profit(prices):
    min_price = float("inf")
    best_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        best_profit = max(best_profit, profit)

    return best_profit

print(max_profit([1,4,6,7,8,9,10]))

'''
How to recognize this pattern in a new question

Look for wording such as “maximum so far,” “minimum seen before,” “best value up to this point,” “running total,” “count while scanning,”
or “find the best result in one pass.”

The deeper signal is this:

If the answer for the current element depends on a summary of earlier elements, try maintaining that summary instead of repeatedly scanning the past.

For example, “find the largest value” needs a maximum. “Count even numbers” needs a counter. “Find the best stock profit” needs a minimum and a best profit.
The code changes, but the thinking pattern is the same.

Your first practice

'''

# Find the minimum: Given a non-empty array, return its smallest element. Handle negative numbers correctly.

def min_val(values):
    smallest = values[0]
    for val in values:
        if val < smallest:
            smallest = val
        else: 
            continue
    return smallest
print(min_val([2,3,4,5,6,7]))

# inbuilt function
print(min(4,5,6,7,8,9))

# Count values: Given an array, return how many numbers are greater than 10. What single variable do you need?

def greater(numbers):
    count = 0
    for num in numbers:
        if num > 10:
            count += 1
    return count
print(greater([10,14,2,4,15]))

# Best stock profit: Reimplement the problem above from memory, then test [7, 6, 4, 3, 1], [2, 4, 1], and [].
def max_profit(prices):
    min_price = float("inf")
    best_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        best_profit = max(best_profit, profit)

    return best_profit

print(max_profit([]))
print(max_profit([2,4,1]))
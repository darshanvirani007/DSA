# Two Sum — finding two numbers that add up to a target

'''

The problem

You have a list of numbers:

numbers = [2, 7, 11, 15]
target = 9

Find two numbers that add up to 9.

Here, 2 + 7 = 9, so the answer is 2 and 7.

First, solve it like a human and then We can turn this into an algorithm:

Pick one number.

Try adding it to each number after it.

If the sum equals the target, return their indexes

'''

def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]

    return []

print(two_sum([2, 7, 11, 15], 9))

def all_two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1
    answers = []

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            answers.append([left, right])
            left += 1
            right -= 1

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return answers


numbers = [1, 2, 4, 6, 8, 11]

print(all_two_sum_sorted(numbers, 10))

def twoSum_hash(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

print(twoSum_hash(numbers,10))
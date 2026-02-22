"""
lab_1d.py

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Derived from LeetCode problem: https://leetcode.com/problems/two-sum/ (leetcode easy)
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    for j in nums:
        for i in nums:
            if (i + j) == target:
                sum = i + j
                ind1 = nums.index(i)
                ind2 = nums.index(j)
                print(f"Because nums[{j}] + nums[{i}] == {sum}, we return [{j}, {i}].")
                result = [ind2, ind1]
                return result
                break
            else:
                continue
    return []  # In case there is no solution, though the problem guarantees one exists.


# Example usage:
def main():
    nums = [2, 7, 11, 15]
    target = 29
    result = two_sum(nums, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")

if __name__ == "__main__":
    main()
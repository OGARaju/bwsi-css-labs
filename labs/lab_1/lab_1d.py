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
                sum = str(sum)
                ind1 = nums.index(i)
                ind1= str(ind1)
                ind2 = nums.index(j)
                ind2 = str(ind2)
                i = str(i)
                j = str(j)
                print("Because nums[" + j + "] + nums[" + i + "] == " + sum + ", we return [" + j + ", " + i + "].")
                result = "[" + ind2 + ", " + ind1 + "]"
                return result
                break
            else:
                continue

# Example usage:
def main():
    nums = [2, 7, 11, 15]
    target = 13
    result = two_sum(nums, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")

if __name__ == "__main__":
    main()
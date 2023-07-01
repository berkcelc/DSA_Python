
# brute force solution

def two_sum(nums:list, target:int):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

def two_sum1(nums:list, target:int):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


import unittest

class TestTwoSum(unittest.TestCase):
    def test_example1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        self.assertEqual(two_sum1(nums, target), expected)

    def test_example2(self):
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        self.assertEqual(two_sum1(nums, target), expected)

    def test_example3(self):
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        self.assertEqual(two_sum1(nums, target), expected)

if __name__ == '__main__':
    unittest.main()

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = {}

        for i in range(len(nums)):
            if dictionary.__contains__(nums[i]):
                dictionary[nums[i]] += 1
            else:
                dictionary[nums[i]] = 0

        return max(dictionary, key=dictionary.get)


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.majorityElement([3, 2, 3]))
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))


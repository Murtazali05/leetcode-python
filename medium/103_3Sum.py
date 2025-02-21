from typing import List

"""
Time complexity: O(n^2)
Space complexity: O(n)
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return [list(triplet) for triplet in result]


if __name__ == '__main__':
    # begin
    s = Solution()
    answer = s.threeSum([-1, 0, 1, 2, -1, -4])
    print("Example 1: ", answer)

    answer = s.threeSum([0, 1, 1])
    print("Example 2: ", answer)

    answer = s.threeSum([0, 0, 0])
    print("Example 3: ", answer)

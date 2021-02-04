from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        non_zero_elem_index = 0

        while i < len(nums) - 1:
            if nums[i] == 0:
                if i > non_zero_elem_index:
                    non_zero_elem_index = i
                while non_zero_elem_index < len(nums) - 1 and nums[non_zero_elem_index] == 0:
                    non_zero_elem_index += 1
                nums[i], nums[non_zero_elem_index] = nums[non_zero_elem_index], nums[i]
            i += 1

        print(nums)


if __name__ == '__main__':
    # begin
    s = Solution()
    s.moveZeroes([0, 1, 0, 3, 12])

# space complexity: O(1)
# time complexity: O(n)
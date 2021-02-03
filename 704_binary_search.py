from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while right - left > 1:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1


if __name__ == '__main__':
    # begin
    s = Solution()
    answer = s.search([-1, 0, 3, 5, 9, 12], 2)
    print(answer)

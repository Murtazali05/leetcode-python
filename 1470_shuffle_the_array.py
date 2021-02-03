from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [None] * 2 * n
        k = 0
        for i in range(n):
            result[k] = nums[i]
            result[k + 1] = nums[n + i]
            k += 2

        return result


if __name__ == '__main__':
    # begin
    s = Solution()
    answer = s.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4)
    print(answer)

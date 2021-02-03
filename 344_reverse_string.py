from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            tmp = s[i]
            s[i] = s[n - i - 1]
            s[n - i - 1] = tmp

        print(s)


if __name__ == '__main__':
    # begin
    s = Solution()
    s.reverseString(["h", "e", "l", "l", "o"])
    s.reverseString(["H", "a", "n", "n", "a", "h"])

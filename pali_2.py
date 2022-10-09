from operator import length_hint
from typing import List
min_num=100000000
ret = list() # the overall substring
ans = list() # the single substring
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        ret = list()
        ans = list()

        def isPalindrome(i: int, j: int) -> int:
            if i >= j:
                return 1
            return isPalindrome(i + 1, j - 1) if s[i] == s[j] else -1

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return
            
            for j in range(i, n):
                if isPalindrome(i, j) == 1:
                    ans.append(s[i:j+1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        isPalindrome.cache_clear()
        return ret

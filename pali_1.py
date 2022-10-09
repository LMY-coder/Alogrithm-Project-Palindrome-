from operator import length_hint
from typing import List
min_num=100000000
ret = list() # the overall substring
ans = list() # the single substring
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

#depth first search
        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return
            
            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret

if __name__ == '__main__':
    s = Solution()
    stri=str(input()) # data input
    print(s.partition(stri)) # data output
    print("\n")
    k=0
    for k in range(k, len(ret)):
                if len(ret[k])<min_num:
                    min_num=len(ret[k])
    l=0
    str_f=""
    for l in range(l, len(ret)):
        str_f+=','.join(ret[l])+"\n"
    print(str_f)
    print(min_num)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_ptr = 0
        s_ptr = 0
        cnt = 0
        while (g_ptr < len(g) and s_ptr < len(s)):
            if (g[g_ptr] <= s[s_ptr]):
                g_ptr += 1
                s_ptr += 1
                cnt+=1
            else:
                s_ptr += 1
        return cnt
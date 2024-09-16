class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        curr = 0
        index_dict = {}
        max_len = 0
        while(curr <= len(s)-1):
            if s[curr] in index_dict and index_dict[s[curr]] >= start:
                start = index_dict[s[curr]] + 1
                index_dict[s[curr]] = curr
            else:
                index_dict[s[curr]] = curr
            curr_len = curr - start + 1
            max_len = max(max_len,curr_len)
            curr += 1
        return max_len
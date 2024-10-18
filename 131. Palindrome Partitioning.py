class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def recurse(curr_ind, curr_star, curr_subs):
            if curr_ind==len(s)-1:
                if s[curr_star:] == s[curr_star:][::-1]:
                    curr_subs.append(s[curr_star:])
                    all_subs.append(curr_subs)
                return

            if s[curr_star:curr_ind+1] == s[curr_star:curr_ind+1][::-1]:
                recurse(curr_ind+1, curr_ind+1, curr_subs + [s[curr_star:curr_ind+1]])
                recurse(curr_ind+1, curr_star, curr_subs)
            else:
                recurse(curr_ind+1, curr_star, curr_subs)
            return 
            
        curr_ind = 0
        curr_star = 0
        curr_subs = []
        all_subs = []
        recurse(curr_ind, curr_star, curr_subs)
        return all_subs
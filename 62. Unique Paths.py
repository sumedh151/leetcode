class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # no_of_right = n-1
        # no_of_down = m-1
        # return math.comb(m+n-2,m-1)*math.comb(n-1,n-1)

        def recurse(curr_x, curr_y):
            if curr_x == m-1 and curr_y == n-1:
                return 1
            elif curr_x==m-1:
                return 1
            elif curr_y==n-1:
                return 1
            else:
                if paths[curr_x][curr_y] != -1:
                    return paths[curr_x][curr_y]
                paths[curr_x][curr_y] = recurse(curr_x, curr_y + 1) + recurse(curr_x + 1, curr_y)
                return paths[curr_x][curr_y]

        curr_x = 0
        curr_y = 0
        paths = [ [-1]*n for i in range(m)]
        total_paths = recurse(curr_x, curr_y)
        return total_paths
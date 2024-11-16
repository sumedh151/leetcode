# https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

############################
####### my approach ########
############################

def knapSack(capacity = 4, val = [1,2,3], wt = [4,5,1]):
    # code here
    def recurse(ind, curr_wt, curr_val):
        if curr_wt > capacity:
          return 0
        if ind == len(val):
          return curr_val
        max_val1 = recurse(ind+1, curr_wt+wt[ind], curr_val+val[ind])
        max_val2 = recurse(ind+1, curr_wt, curr_val)
        return max(max_val1, max_val2)        
    curr_wt = 0
    curr_val = 0
    ind = 0
    max_val = 0
    max_val = recurse(ind, curr_wt, curr_val)
    return max_val

print(knapSack(capacity = 4, val = [1,2,3], wt = [4,5,1]))


# memoization
def knapSack(capacity=4, val=[1, 2, 3], wt=[4, 5, 1]):
    memo = {}
    def recurse(ind, curr_wt, curr_val):
        if (ind, curr_wt) in memo:
            return memo[(ind, curr_wt)]
        if curr_wt > capacity:
            return 0
        if ind == len(val):
            memo[(ind, curr_wt)] = curr_val
            return curr_val
        include_val = recurse(ind + 1, curr_wt + wt[ind], curr_val + val[ind])
        exclude_val = recurse(ind + 1, curr_wt, curr_val)
        result = max(include_val, exclude_val)
        memo[(ind, curr_wt)] = result
        return result
    return recurse(0, 0, 0)

print(knapSack(capacity=4, val=[1, 2, 3], wt=[4, 5, 1]))









############################
####### AV approach ########
############################

def knapSack(capacity=4, val=[1, 2, 3], wt=[4, 5, 1], n=3):
    # print('here')
    if n==0 or capacity==0:
        return 0
    if wt[n-1] <= capacity:
        return max(val[n-1] + knapSack(capacity - wt[n-1] , val, wt, n-1),
                knapSack(capacity, val, wt, n-1) 
            )
    elif wt[n-1] > capacity:
        return knapSack(capacity, val, wt, n-1) 
print(knapSack(capacity=4, val=[1, 2, 3], wt=[4, 5, 1], n=3))


# memoization
memo = {}
def knapSack(capacity=4, val=[1, 2, 3], wt=[4, 5, 1], n=3):
    if n==0 or capacity==0:
        return 0
    if memo.get((n,capacity),-1) != -1:
        return memo[(n,capacity)]
    if wt[n-1] <= capacity:
        memo[(n,capacity)] =  max(val[n-1] + knapSack(capacity - wt[n-1] , val, wt, n-1),
                knapSack(capacity, val, wt, n-1) 
            )
        return memo[(n,capacity)]
    elif wt[n-1] > capacity:
        memo[(n,capacity)] =  knapSack(capacity, val, wt, n-1) 
        return memo[(n,capacity)]

print(knapSack(capacity=4, val=[1, 2, 3], wt=[4, 5, 1], n=3))
print(memo)
from collections import defaultdict
class Solution(object):
    def numberOfSubsequences(self, nums):
        n = len(nums)
        count = 0
        product_pairs= defaultdict(list)
        for p in range(n):
            for q in range(p + 4, n): 
                product = nums[p] * nums[q]
                product_pairs[product].append((p, q))
        
        for r in range(2,n):
            for s in range(r + 4, n):  
                product = nums[r] * nums[s]
                for p, q in product_pairs[product]:
                        if p+1<r and r+1<q and q+1<s:  
                            count += 1
                        if p+1>=r:
                            break
        return count

            
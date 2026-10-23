class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]]
        for i in range(len(nums)):
            for r in range(len(res)):
                res.append([nums[i]] + res[r])
        return res
            
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        '''
        heapify then pop one by one

        O(n) total, better than O(nlogn)
        '''
        h = nums

        heapq.heapify(h)

        for i in range(len(nums) - k):
            heapq.heappop(h)
        
        return heapq.heappop(h)


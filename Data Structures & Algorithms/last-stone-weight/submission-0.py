class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while stones:
            l1 = heapq.heappop(stones)
            if not stones:
                return -l1
            l2 = heapq.heappop(stones)

            heapq.heappush(stones, l1 - l2)



        return 0
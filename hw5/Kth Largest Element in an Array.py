import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            # If heap grows larger than k, remove the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        # The root element of the heap is the kth largest
        return min_heap[0]

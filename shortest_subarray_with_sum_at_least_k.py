from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return -1
        de_queue = deque()
        min_length = len(nums) + 1
        prefix_sum_array = [0]
        for num in nums:
            prefix_sum_array.append(prefix_sum_array[-1] + num)
        for i in range (len(nums) + 1):
            while de_queue and prefix_sum_array[i] - prefix_sum_array[de_queue[0]] >= k:
                min_length = min(min_length, i - de_queue.popleft())
            while de_queue and prefix_sum_array[i] <= prefix_sum_array[de_queue[-1]]:
                de_queue.pop()
            de_queue.append(i)
        if min_length <= len(nums):
            return min_length
        return -1

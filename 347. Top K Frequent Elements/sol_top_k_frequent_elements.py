from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        # count the freq of each number in the input array and store as a dict
        counter = Counter(nums)
        heap = []

        for num, freq in counter.items():
            # push to the heap the inv freq and num, creating a min heap
            heapq.heappush(heap, (-freq, num))

        result = []
        for _ in range(k):
            # pop/append the heap vals
            # since it's smallest, pop the most negative num/ most freq num
            result.append(heapq.heappop(heap)[1])

        return result
    
'''
space-complexity: O(n + k)
nums counter is O(n),
result is O(k)

time-complexity: O(k * log(n))
counter is O(n)
heap/heappush is O(n * log(n))
heappop is O(log(n))
so total is O(k * log(n))

NOTE: I need to study up on time complexity and space complexity
because I'm having a hard time calculating it without using
chatgpt... which is really lame. I found a video on it and
I'll see if that sparks old knowledge, and if not, I'll
have to do a more indepth practice.
'''
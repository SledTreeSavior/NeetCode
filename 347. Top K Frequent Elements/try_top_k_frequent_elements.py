from ast import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)
        for num in nums:
            if num not in num_count.keys():
                num_count[num] = 1
            else:
                num_count[num] += 1

        print(num_count)
        sorted_num_count = sorted(num_count.items(), key=lambda x:x[1], reverse=True)
        print(sorted_num_count)

        output = []
        for item in sorted_num_count[:k]:
            output.append(item[0])

        return output
    
'''
time-complexity: O(n * log(n))
This is because the first for loop is O(n),
the sorted() function has a complexity of O(n * log(n)),
creating the output is O(k),
so the overall time-complexity is O(n * log(n))

space-complexity: O(n) + O(n) + O(k)
This is because num_count is O(n),
sorted_num_count is O(n),
and output is O(k)

Overall, this solution wasn't bad.
It performed okay as far as runtime,
but it used quite a bit of memory.
'''
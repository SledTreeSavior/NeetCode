from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        char_dict = {}

        for word in strs:
            char_dict.update({word:{*word}})
            
        for word in strs:
            chunk = [k for k, v in char_dict.items() if v == {*word}]
            if chunk not in output:
                output.insert(0, chunk)

        return output
    
'''
N = total number of chars in all the words
M = number of unique anagram groups

time-complexity: O(N*M) or essentially O(N^2)
space-complexity: O(N) + O(M)

The problems here are obvious. I have a for loop, followed by a nested for loop.
There really isn't a situation where this is a good idea.
I need to minimize the number of times I do this.
It's just a showing of my lack of knowledge of data structures.

This solution also doesn't pass all test cases, only 41/120...

'''
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        # create a dictionary which has key values defaulted to lists
        anagram_map = defaultdict(list)

        for word in strs:
            # sort the word and combine the sorted chars into a string
            sorted_word = ''.join(sorted(word))
            # add the word to the value list associated with the sorted word key
            anagram_map[sorted_word].append(word)

        # return the list representation of the dictionary
        return list(anagram_map.values())


'''
N = the number of words in the input list
K = the maximum length of a word

time-complexity: O(NKlog(K))
    Sorting each word takes O(K*log(K)) time, and we do this for each of the N words.
space-complexity: O(N*K), as we store the anagram groups in a dictionary.

This approach makes a lot of sense to me after working thorugh it.
It similarly uses a dictionary, but stores the sorted word as the key,
and the anagram groups as the value. 
Sorting the word makes more sense than storing the chars in a set,
and storing the anagram groups as the value allows you to build upon it,
as opposed to just having a single string.
'''
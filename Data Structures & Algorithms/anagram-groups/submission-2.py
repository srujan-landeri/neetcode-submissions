class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_anagrams = dict()
        for word in strs:

            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1

            key = tuple(count)
            if key not in sorted_anagrams:
                sorted_anagrams[key] = []

            sorted_anagrams[key].append(word)

        return list(sorted_anagrams.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_anagrams = dict()
        for word in strs:
            sorted_str = "".join(sorted(word))
            if sorted_str not in sorted_anagrams:
                sorted_anagrams[sorted_str] = [word]

            else:
                sorted_anagrams[sorted_str].append(word)

        return_list = []
        for val in sorted_anagrams.values():
            return_list.append(val)

        return return_list
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        results = []
        processed = {}

        for word in strs: 
            key = ''.join(sorted(word))
            if key not in processed:
                processed[key] = []
            
            processed[key].append(word)

        for val in processed.values():
            results.append(val)

        return results

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        res = []
        for word in strs:
            freqCount = [0] * 26

            for i in range(len(word)):
                freqCount[ord(word[i]) - ord('a')] +=  1
            
            groups[str(freqCount)].append(word)
        
        for k, v in groups.items():
            res.append(v)
        return res


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        check = set()
        groups = defaultdict(list)
        for s in strs:
            letters = [0] * 25

            for i in range(len(s)):
                letters[ord('a') - ord(s[i])] += 1
            
            key = ""
            for element in letters:
                key = key + str(element) + ","
               
            groups[key].append(s)
        
        res = []
        for key,value in groups.items():
            res.append(groups[key])
        
        return res
            


            
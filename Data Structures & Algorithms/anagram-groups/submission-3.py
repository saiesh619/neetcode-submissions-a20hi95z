class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        groupedAnagrams = {}
        for values in strs:
            print(values)
            word = values 
            count = [0]*26
            key = ""
            for letters in word:
                count[ord(letters) - ord('a')]+= 1
            for c in count:
                key = key + str(c) + ","
            if key not in groupedAnagrams:
                groupedAnagrams[key] = []
            groupedAnagrams[key].append(word)
        
        for key, words in groupedAnagrams.items():
            print("key", key)
            print("words", word)
        for key in groupedAnagrams.values():
           result.append(key)
        print(groupedAnagrams)
        return result
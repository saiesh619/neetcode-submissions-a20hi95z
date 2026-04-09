class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            encode += str(len(s)) + "$" + s  
        return encode

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        n = len(s)
        while i < n:
            dL = ""
            while i < n and s[i] != "$":
                dL = dL + s[i]
                i += 1
            print(dL)                
            m = int(dL)
            j = 0
            decode = ""
            i = i + 1
            while i < n and j < m:
                decode += s[i]                
                j += 1
                i += 1
            res.append(decode)
            
        
        return res
            

            

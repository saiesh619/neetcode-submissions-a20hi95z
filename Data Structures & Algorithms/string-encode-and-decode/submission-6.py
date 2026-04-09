class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for element in strs:
            encodedString =  encodedString + str(len(element)) +  "#" + element  
        return encodedString


    def decode(self, s: str) -> List[str]:        
        n = len(s)
        i = 0
        res = []
        print("s = ",s)
        decodedString = ""
        length = ""
        while i < n:
            if s[i] != "#":
                length = length + s[i] 
                i+= 1           
            else:
                print("length", length)
                lengthOfDecoded = int(length) - 1
                length = ""
                decodedString = ""
                i += 1
                while i < n and lengthOfDecoded >= 0:
                    decodedString = decodedString + s[i]
                    i += 1
                    lengthOfDecoded -= 1
            
           
                res.append(decodedString)
        return res
                



            
            

                

        
        return res
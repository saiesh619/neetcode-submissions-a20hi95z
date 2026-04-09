class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        previousElement = set()
        
        for values in nums:
            if values in previousElement:
                return True
            else:
                previousElement.add(values)
        return False
         
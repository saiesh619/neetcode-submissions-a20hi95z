class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1
        res = []
        while left < right:
            s = numbers[left] + numbers[right]
            if s > target:
                right = right - 1 
            elif s < target:
                left = left + 1 
            else:
                res.append(left+1)
                res.append(right+1)
                break;
        return res
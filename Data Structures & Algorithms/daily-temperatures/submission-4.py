class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        
        n = len(temperatures)
        res = [0]*n

        for i in range(n):

            while st and temperatures[i] > temperatures[st[-1]]:
                index = st[-1]
                diff = i - index
                print(index,st)
                res[index] = diff
                print('index',index)
                print('ans',diff)
                st.pop()
            print('new\n')
            st.append(i)

        return res
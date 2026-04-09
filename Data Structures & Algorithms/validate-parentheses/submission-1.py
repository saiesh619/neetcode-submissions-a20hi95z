class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        openToClose = {'}':'{', ']':'[', ')':'('}
        for bracket in s:
            if bracket in openToClose:
                if st and st[-1] == openToClose[bracket]:
                    st.pop()
                else:
                    return False
            else:
                st.append(bracket)
        return len(st) == 0
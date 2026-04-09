class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        res = 0
        for element in tokens:
            if element == "+":                
                st.append(st.pop() + st.pop())
            elif element == "-":
                b,a = st.pop(), st.pop()                
                st.append(a - b)
            
            elif element == "*":
                b,a = st.pop(), st.pop()                
                st.append(a*b)
            
            elif element == "/":
                b,a = st.pop(), st.pop()
                
                st.append(int(float(a) / b))
            else:
                st.append(int(element))
        
        return st[0]
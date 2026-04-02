class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        op = { ")" : "(", "]" : "[", "}" : "{" }
        for i in s:
            if i in op:
                if st and op[i] == st[-1]:
                    st.pop()
                else: return False
                
            else:
                st.append(i)
        return not st

        
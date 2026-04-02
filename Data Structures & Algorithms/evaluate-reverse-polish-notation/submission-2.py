class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:

            

            match t:
                case "+":
                    a = int(st[-1])
                    b = int(st[-2])
                    st.pop()
                    st.pop()
                    st.append(a+b)
                case "*":
                    a = int(st[-1])
                    b = int(st[-2])
                    st.pop()
                    st.pop()
                    st.append(a*b)
                case "-":
                    a = int(st[-1])
                    b = int(st[-2])
                    st.pop()
                    st.pop()
                    st.append(b-a)
                case "/":
                    a = int(st[-1])
                    b = int(st[-2])
                    st.pop()
                    st.pop()
                    st.append(int(b/a))
                case _:
                    st.append(int(t))
        
        return st[0]


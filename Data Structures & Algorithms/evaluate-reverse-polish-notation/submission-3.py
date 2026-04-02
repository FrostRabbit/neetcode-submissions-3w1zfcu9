class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        l = ["+","*","-","/"]
        for t in tokens:

            if t in l:
                a = int(st[-1])
                b = int(st[-2])
                st.pop()
                st.pop()
            match t:
                case "+":
                    st.append(a+b)
                case "*":
                    st.append(a*b)
                case "-":
                    st.append(b-a)
                case "/":
                    st.append(int(b/a))
                case _:
                    st.append(int(t))
        
        return st[0]


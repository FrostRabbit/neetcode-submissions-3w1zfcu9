class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res =[0] * len(temperatures)
        for i,v in enumerate(temperatures):
            while st and v > st[-1][1]:
                topI, topV = st.pop()
                res[topI] = i - topI
            st.append((i,v))
        return res
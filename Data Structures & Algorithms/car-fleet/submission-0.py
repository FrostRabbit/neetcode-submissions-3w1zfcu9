class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pa = [(p,s) for p,s in zip(position, speed)]
        pa.sort(reverse=True)
        st = []
        for p,s in pa:
            st.append((target-p)/s)
            if len(st) >= 2 and st[-1]<=st[-2]:
                st.pop()
        return len(st)
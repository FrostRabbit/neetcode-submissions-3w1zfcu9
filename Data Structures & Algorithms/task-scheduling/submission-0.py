class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0]*26
        for t in tasks:
            count[ord(t)-ord('A')] += 1
        max_f = max(count)
        max_c = 0
        for c in count:
            max_c += 1 if c == max_f else 0
        time = (max_f-1)*(n+1) + max_c
        return max(len(tasks),time)
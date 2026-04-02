class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            chars = [0] *26
            for c in i:
                chars[ord(c)-ord('a')]+=1
            hashmap[tuple(chars)].append(i)
        return list(hashmap.values())
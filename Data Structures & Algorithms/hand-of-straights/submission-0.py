class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: return False

        count = Counter(hand)
        hand.sort()
        for n in hand:
            if count[n] > 0:
                for i in range(n, n+groupSize):
                    if count[i] < 1:
                        return False
                    count[i]-=1
        return True
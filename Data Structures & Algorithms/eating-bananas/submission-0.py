class Solution:

    def possible(self, piles: List[int], h: int, k:int) -> bool:
        i: int = 0
        while i < len(piles):
            remainder: int = piles[i]%k
            quotient: int = int(piles[i]/k)
            h -= (quotient + 1) if remainder > 0 else quotient
            i+=1
        if h >=0:
            return True
        else:
            return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l: int = 1
        mid: int = 0
        r: int = max(piles)
        minK: int = 99999999999
        while l<=r:
            mid = int(l + int((r-l)/2))
            if self.possible(piles, h, mid):
                minK = mid
                r=mid-1
            else:
                l=mid+1
        return minK
# if h is less than len of piles < not possible according to contraints.
# h is 10^9
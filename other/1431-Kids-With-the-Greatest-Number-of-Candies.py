class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatestCandies = []

        for candy in candies:
            if candy + extraCandies >= max(candies):
                greatestCandies.append(True)
            else:
                greatestCandies.append(False)
        return greatestCandies
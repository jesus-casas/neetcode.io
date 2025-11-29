2025-11-29

[Leetcode Link](https://leetcode.com/problems/find-the-difference-of-two-arrays/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Hash Map & Set]] - [[look back]] - [[pythonic]]

TC: O(n * m)

SC: O(n + m)

## Code Solution: 

```python
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [self.getElementsOnlyInFirstList(nums1, nums2),self.getElementsOnlyInFirstList(nums2,nums1)]

    def getElementsOnlyInFirstList(self,nums1,nums2):
        onlyInNums1 = set()

        for num in nums1:
            existInNums1 = False
            
            for x in nums2:
                if x == num:
                    existInNums1 = True
                    break
            if not existInNums1:
                onlyInNums1.add(num)
        return list(onlyInNums1)

```

## Notes:
- 

## Pythonic Code Solution: 

TC: O(n + m)

SC: O(n + m)

```python
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2),list(set2 - set1)]
```

## Notes:
- 

2025-10-01

[Leetcode Link](https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Two Pointers]] - [[Look Back]]

TC: O(N)

SC: O(N)

## O(N): Solution:
```python
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap = {}
        count = 0

        for i in range(len(nums)):
            res = k - nums[i]
            if res in hashmap:
                count += 1
                if hashmap[res] == 1:
                    hashmap.pop(res)
                else:
                    hashmap[res] -= 1
            else:
                hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
        return count
```

## O(nlogn) Sol Sort:

```python
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        count = 0

        while i < j:
            total = nums[i] + nums[j]
            if total == k:
                count += 1
                i += 1
                j -= 1
            elif total > k:
                j -= 1
            else:
                i += 1

        return count
```



## Notes:
- 

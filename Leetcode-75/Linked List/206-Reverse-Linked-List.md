2026-01-14

[Leetcode Link](https://leetcode.com/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75)

Tags: [[Linked List]]

TC: O(n)
## Code Solution: 

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
```

## Notes:
- 

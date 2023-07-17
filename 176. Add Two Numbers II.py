# https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1,stack2=[],[]
        while l1:
            stack1.append(l1.val)
            l1=l1.next

        while l2:
            stack2.append(l2.val)
            l2=l2.next

        carry=0
        result=None

        while stack1 or stack2 or carry:
            sum_val=carry
            if stack1:
                sum_val+=stack1.pop()
            if stack2:
                sum_val+=stack2.pop()
            
            node=ListNode(sum_val%10)
            node.next=result
            result=node
            carry=sum_val//10
        return result
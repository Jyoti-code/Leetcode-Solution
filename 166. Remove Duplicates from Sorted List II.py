# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return
        else:
            a=[]
            b=[]
            temp=head
            while temp:
                a.append(temp.val)
                temp=temp.next
            for i in a:
                if a.count(i)==1:
                    b.append(i)
            if b==[]:
                return
            else:
                headnode=ListNode(b[0])
                newnode=headnode
                for i in range(1,len(b)):
                    newnode.next=ListNode(b[i])
                    newnode=newnode.next
                return headnode
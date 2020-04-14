'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def append(self, val):
        self.head = None
        self.last_node = None
        if self.last_node is None:
            self.head = ListNode(val)
            self.last_node = self.head
        else:
            self.last_node.next = ListNode(val)
            self.last_node = self.last_node.next
obj=Solution()
def middleNode(self, head: ListNode) -> ListNode:
        res=ListNode(head)
        current=head
        length=0
        while current:
            current=current.next
            length=length+1
        current=head
        for i in range((length-1)//2):
            current=current.next
        while current:
            if current:
                if length%2==0:
                    obj.append(self,current.next.val)
                    current=current.next
                else:
                    obj.append(self,current.val)
                    current=current.next
            else:
                return None
        return ListNode
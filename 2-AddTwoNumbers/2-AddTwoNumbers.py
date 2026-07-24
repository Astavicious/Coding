# Last updated: 24/07/2026, 17:03:01
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def addTwoNumbers(self, l1, l2):
8        """
9        :type l1: Optional[ListNode]
10        :type l2: Optional[ListNode]
11        :rtype: Optional[ListNode]
12        """
13        dummy=ListNode()
14        current=dummy
15        carry=0
16        while l1 or l2 or carry:
17            #to get the digits
18            dl1=0
19            dl2=0
20            if l1:
21                dl1=l1.val
22            if l2:
23                dl2=l2.val
24            total=dl1+dl2+carry
25            #summation and carry for the next node
26            carry=total//10
27            ans=total %10
28            #now moving the current node forward and adding the digit
29            current.next=ListNode(ans)
30            current=current.next
31            #now moving l1 and l2 forward
32            if l1:l1=l1.next
33            if l2:l2=l2.next
34        return dummy.next
35
36
37
38        
39        
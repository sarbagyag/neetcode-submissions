"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mainNodeAndNoPointerHashMap={None:None}

        curr=head

#1st Pass to Map Node -> Value Node (no pointers)
        while curr:
            nodeWithValueOnly=Node(curr.val)
            mainNodeAndNoPointerHashMap[curr]=nodeWithValueOnly
            curr=curr.next
        
        curr=head

#2nd Pass, Re-link the Pointers
        while curr:
            toAssignPointers=mainNodeAndNoPointerHashMap[curr]
            toAssignPointers.next=mainNodeAndNoPointerHashMap[curr.next]
            toAssignPointers.random=mainNodeAndNoPointerHashMap[curr.random]
            curr=curr.next
        
        return mainNodeAndNoPointerHashMap[head]
            
            
            
            

        

        

            
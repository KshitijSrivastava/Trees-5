
 ### Problem1 Populating Next Right Pointers in Each Node
 
 # (https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)



"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        
        #add root to the queue
        queue = []
        queue.append( root )
        
        child_queue = []
        
        #continue while the queue is not empty
        while len(queue) != 0:
            #pop the element from the queue
            node = queue.pop(0)
            
            #insert the left child to the child queue
            if node.left:
                child_queue.append( node.left )
                
            #insert the right child to the child queue
            if node.right:
                child_queue.append( node.right )
                
            #if the length of the queue is not equal to 0
            #point it to the element in the front of the queue
            if len(queue) != 0:
                node.next = queue[0]
            else:
                #last node of the row
                node.next = None
                # queue not is ther child row
                queue = child_queue
                #child row is not empty
                child_queue = []
        return root
                
        
            
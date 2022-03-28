## Problem2 Recover Binary Search Tree
# (https://leetcode.com/problems/recover-binary-search-tree/)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, root, sorted_arr):
        if root is None:
            return
        
        self.inorder(root.left, sorted_arr)
        
        sorted_arr.append( root )
        
        self.inorder(root.right, sorted_arr)
        
        
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        sorted_arr = []
        self.inorder(root, sorted_arr)
        
        values = [ node.val for node in sorted_arr ]
        values.sort()
        
        first_left = None
        first_right = None
        first = None
        
        second_left = None
        second_right = None
        second = None
        
        
        for v, node in zip( values,  sorted_arr):
            if v != node.val:
                #print(v)
                
                #save the node values which are not sorted
                if first == None:
                    first = node
                    first_left = node.left
                    first_left = node.right
                else:
                    second = node
                    second_left = node.left
                    second_right =  node.left
                    
        #print(first, second)
        #replacing the both the node values
        first.val, second.val = second.val, first.val
                    
                
                
        
"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def __init__(self):
        # start of merged list.
        self.head = None
        
        # tail of merged list.
        self.tail = None
        
    def insert_at_tail(self, node):
        
        # stop pointing to the next node.
        node.next = None
        
        # list is empty.
        if self.head is None:
            # update head.
            self.head = node
            
            # update tail.
            self.tail = node
        # list is not empty.
        else:
            # add to the end of list.
            self.tail.next = node
            
            # update tail.
            self.tail = node
        
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # while both list has elements, 
        # we need to compare them and insert 
        # the one with the lowest value.
        
        curr_l1 = l1
        
        curr_l2 = l2
        
        while curr_l1 is not None and curr_l2 is not None:
            
            # we should insert curr_l1 in the merged list.
            if curr_l1.val < curr_l2.val:
                
                # maintain referce to next node.
                temp = curr_l1.next
                
                # insert curr_l1 into merged list.
                self.insert_at_tail(curr_l1)
                
                # update curr_l1
                curr_l1 = temp
                
            else:
                # maintain referce to next node.
                temp = curr_l2.next
                
                # insert curr_l1 into merged list.
                self.insert_at_tail(curr_l2)
                
                # update curr_l1
                curr_l2 = temp
                
        # at this point in the algorithm, either:
        # 1. both source lists are empty.
        # 2. the first list is empty, but the second is not.
        # 3. the second list is empty, but the first is not.

        # if there are remaining nodes in the first list. 
        # copy it over.
        while curr_l1 is not None:
            temp = curr_l1.next
            self.insert_at_tail(curr_l1)
            curr_l1 = temp
            
        # if there are remaining nodes in the second list. 
        # copy it over.
        while curr_l2 is not None:
            temp = curr_l2.next
            self.insert_at_tail(curr_l2)
            curr_l2 = temp
            
        return self.head
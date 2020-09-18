import pdb
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
         
class Solution:
    def __init__(self):
        self.head = None
    def seq4(self):
        head = ListNode(val=1)
        Node2 = ListNode(val=2)
        Node3 = ListNode(val=3)
        Node4 = ListNode(val=4)
        
        head.next = Node2
        Node2.next = Node3
        Node3.next = Node4
        self.head = head
    def printList(self, head):
        string = ''
        iterator = ListNode()
        iterator.next = head
        while iterator.next != None:
            string += str(iterator.next.val)
            string += '->'
            iterator.next = iterator.next.next
            #pdb.set_trace()
        print(string)
    def swapPairs(self, head: ListNode) -> ListNode:
        def swap(iterator, trail, swapped, newhead):
            # save the next node
            next_save = ListNode()
            next_save.next = iterator.next.next
            # repoint the current 2nd node to the previous node
            iterator.next.next = trail.next
            # repoint the previous node to the saved next node
            trail.next.next = next_save.next
            
            # point to the new head, if this is the first time swapping
            if not swapped:
                newhead.next = iterator.next
                swapped = True
            
            # reset the iterator and trail for continued iterating
            trail.next = iterator.next
            iterator.next = iterator.next.next
            
            return swapped, newhead
            
        # create a dummy node that allows another traverser to trail
        dummy = ListNode()
        dummy.next = head
        
        # have two traverser nodes, one trailing the other
        trail = ListNode()
        trail.next = dummy
        
        iterator = ListNode()
        iterator.next = head
        
        # counter, will swap on 'odd' integers
        counter = 0
        
        # set new head on first swap
        swapped = False
        newhead = ListNode()
        newhead.next = head
        
        while iterator.next.next != None:
            
            if counter % 2 == 1:
                swapped, newhead = swap(iterator, trail, swapped, newhead)
                
            iterator.next = iterator.next.next
            trail.next = trail.next.next
            counter += 1
            
            print('Counter: ' + str(counter-1))
            self.printList(newhead.next)
            
        if counter % 2 == 1:
            swapped, newhead = swap(iterator, trail, swapped, newhead)
            self.printList(newhead.next)
        if swapped:
            return newhead.next
        else:
            return head
            
def main():
    sol = Solution()
    print('Initializing LL')
    sol.seq4()
    print('Printing initial LL')
    sol.printList(sol.head)
    print('swapping LL')
    sol.head = sol.swapPairs(sol.head)
    sol.printList(sol.head)
    
if __name__ == '__main__':
    main()
    
    
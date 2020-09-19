#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def __init__(self):
        #self.head = None
        self.head = ListNode(1)
        two = ListNode(2)
        three = ListNode(3)
        four = ListNode(4)
        self.head.next = two
        two.next = three
        three.next = four
        
    def show_LL(self, head):
        x = ListNode()
        x.next = head
        LL_str = ''
        while x.next != None:
            LL_str += str(x.next.val)
            LL_str += '->'
            x.next = x.next.next
        LL_str += 'None'
        print(LL_str)

    def swapPairs(self, head: ListNode) -> ListNode:
        # create dummy node
        dummy = ListNode()
        dummy.next = head
        
        # create trailing and heading pointers
        trailing = ListNode() 
        trailing.next = dummy
        heading = ListNode()
        heading.next = head
        
        # variables neeeded for newhead later
        newhead = ListNode()
        newhead.next = heading.next
        swapped = False
        
        # swap heading, and heading's next node positions when counter is even
        counter = 0
        
        # A -> B -> C -> D. Want to swap node B and C.
        # ^    ^
        # |    |
        # T    H
        while heading.next != None:
            if (counter % 2 == 0):
                if heading.next.next == None:
                    break
                # save node D
                save = ListNode()
                save.next = heading.next.next.next
                # point node C to node B
                heading.next.next.next = heading.next
                # point node A to node C
                trailing.next.next = heading.next.next
                # point node B to node D
                heading.next.next = save.next
                # reset headning pointer to what its new position should be
                heading.next = trailing.next.next
                # get new head, if we havent already, set swapped to true
                if not swapped:
                    newhead.next = heading.next
                    swapped = True
            
            # push both traversing pointers forward, incremeent counters
            heading.next = heading.next.next
            trailing.next = trailing.next.next
            counter += 1
        
        return newhead.next
        
        
def main():
    A = Solution()
    A.show_LL(A.head)
    A.head = A.swapPairs(A.head)
    A.show_LL(A.head)

if __name__ == '__main__':
    main()
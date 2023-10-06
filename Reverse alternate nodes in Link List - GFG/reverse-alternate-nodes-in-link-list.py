"""
  reverse alternate nodes and append at the end
  The input list will have at least one element
  Node is defined as
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

"""
class Solution:
    def rearrange(self, head):
        # Code hereListNode
        alternatehead = Node(0)
        cural = alternatehead
        cur = head
        prev = Node(0)
        alter = 0
        while cur is not None:
            if (alter == 1):
                
                cural.next = Node(cur.data)
                cural = cural.next
                
                prev.next = cur.next
                cur = cur.next
                alter = 0
                continue
                
            prev = cur
            cur = cur.next
        
            alter = 1
            
        cur = head
        while cur.next is not None:
            cur = cur.next
        tail = cur
        
       
        reversealternatehead = Node(0)
        
        cur = alternatehead.next
        prev = None
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            # prev.next = nxt
            prev = cur
            cur = nxt
         
       
       
        tail.next = prev
        return head


#{ 
 # Driver Code Starts
# Node Class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class contains node object
class LinkedList:
    # Constructor to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Code execution starts here
if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
            
        Solution().rearrange(llist.head)
        llist.printList()
        t -= 1
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
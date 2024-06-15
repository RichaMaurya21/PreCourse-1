#Time Complexity = O(n) Space Complexity O(n)
class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time in worst case (when iterating to the end).
        """
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time in worst case (when iterating through the list).
        """
        current = self.head
        while current is not None:
            if current.data == key:
                return current
            current = current.next
        return None

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time in worst case (when removing the head or last node).
        """
        if self.head is None:
            return
        
        if self.head.data == key:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next is not None:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next

# Example
if __name__ == "__main__":
    sll = SinglyLinkedList()

    # Append some nodes
    sll.append(10)
    sll.append(20)
    sll.append(30)

    # Find a node
    node = sll.find(20)
    if node:
        print("Node found with value:", node.data)
    else:
        print("Node not found")

    # Remove a node
    sll.remove(20)

    # Check if node was removed
    node = sll.find(20)
    if node:
        print("Node found with value:", node.data)
    else:
        print("Node not found")

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1, list2):
    # Dummy node to simplify code
    dummy = ListNode()
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # If one of the lists is not empty, append the remaining nodes
    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return dummy.next

def print_list(head):
    while head is not None:
        print(head.value, end="->")
        head = head.next
    print("None")

# Example usage:
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

merged_list = merge_sorted_lists(list1, list2)

print("Merged List:", end=" ")
print_list(merged_list)
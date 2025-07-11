"""
Là cấu trúc dữ liệu gồm các nút (node), mỗi nút chứa dữ liệu và một liên kết đến nút kế tiếp.
Thích hợp khi số lượng phần tử thay đổi động, cần thêm/xóa phần tử linh hoạt.
Bad example :(
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Sử dụng
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # Output: 1 -> 2 -> 3 -> None

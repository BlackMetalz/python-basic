"""
Cấu trúc dữ liệu FIFO (First In First Out).
Thao tác chính: enqueue (thêm), dequeue (lấy ra phần tử đầu tiên).
This is understandable xD
"""

from collections import deque

queue = deque()

# Thêm phần tử
queue.append(1)
queue.append(2)

# Lấy phần tử
print(queue.popleft())  # Output: 1
print(queue.popleft())  # Output: 2

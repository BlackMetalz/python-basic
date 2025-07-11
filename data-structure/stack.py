"""
Cấu trúc dữ liệu LIFO (Last In First Out).
Thao tác chính: push (thêm), pop (lấy ra phần tử trên cùng).
Just translate "stack" word to Vietnamese. You will understand how it works.
"""

stack = []

# Thêm phần tử
stack.append(1)
stack.append(2)

# Lấy phần tử
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1

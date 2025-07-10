# Special methods

Dưới đây là **danh sách một số phương thức đặc biệt (special methods hay dunder methods)** phổ biến trong Python, giúp bạn điều khiển hành vi của đối tượng với các toán tử, hàm tích hợp, và cú pháp đặc biệt:

| Phương thức        | Mục đích chính                                       | Ví dụ sử dụng / Ý nghĩa                         |
|--------------------|-----------------------------------------------------|-----------------------------------------------|
| `__init__(self, ...)`       | Khởi tạo đối tượng khi tạo instance mới           | Gán thuộc tính ban đầu cho đối tượng          |
| `__str__(self)`             | Chuỗi biểu diễn thân thiện khi dùng `print()`    | Định nghĩa cách in đối tượng                   |
| `__repr__(self)`            | Chuỗi biểu diễn chính xác, dùng trong debug       | Hiển thị chi tiết đối tượng                     |
| `__del__(self)`             | Hàm hủy đối tượng (destructor)                     | Xử lý khi đối tượng bị xóa                      |
| `__add__(self, other)`      | Toán tử cộng `+`                                   | `a + b` gọi `a.__add__(b)`                      |
| `__sub__(self, other)`      | Toán tử trừ `-`                                   | `a - b` gọi `a.__sub__(b)`                      |
| `__mul__(self, other)`      | Toán tử nhân `*`                                  | `a * b` gọi `a.__mul__(b)`                      |
| `__truediv__(self, other)`  | Toán tử chia `/`                                  | `a / b` gọi `a.__truediv__(b)`                  |
| `__floordiv__(self, other)` | Toán tử chia lấy phần nguyên `//`                 | `a // b` gọi `a.__floordiv__(b)`                |
| `__mod__(self, other)`      | Toán tử modulo `%`                                | `a % b` gọi `a.__mod__(b)`                      |
| `__pow__(self, other)`      | Toán tử lũy thừa `**`                             | `a ** b` gọi `a.__pow__(b)`                      |
| `__lt__(self, other)`       | So sánh nhỏ hơn ``                               | `a > b` gọi `a.__gt__(b)`                        |
| `__ge__(self, other)`       | So sánh lớn hơn hoặc bằng `>=`                     | `a >= b` gọi `a.__ge__(b)`                       |
| `__getitem__(self, key)`    | Truy cập phần tử bằng chỉ số hoặc khóa            | `obj[key]` gọi `obj.__getitem__(key)`           |
| `__setitem__(self, key, value)` | Gán giá trị cho phần tử theo chỉ số hoặc khóa | `obj[key] = value` gọi `obj.__setitem__(key, value)` |
| `__delitem__(self, key)`    | Xóa phần tử theo chỉ số hoặc khóa                   | `del obj[key]` gọi `obj.__delitem__(key)`       |
| `__iter__(self)`            | Trả về iterator cho vòng lặp                        | Cho phép dùng `for x in obj`                      |
| `__next__(self)`            | Lấy phần tử tiếp theo trong iterator                | Dùng trong iterator                              |
| `__call__(self, ...)`       | Khi đối tượng được gọi như hàm                      | `obj()` gọi `obj.__call__()`                     |
| `__len__(self)`             | Độ dài của đối tượng                                | `len(obj)` gọi `obj.__len__()`                   |
| `__contains__(self, item)`  | Kiểm tra phần tử có trong đối tượng hay không      | `item in obj` gọi `obj.__contains__(item)`      |
| `__enter__(self)` / `__exit__(self, exc_type, exc_val, exc_tb)` | Hỗ trợ context manager với `with` | Quản lý tài nguyên khi vào/ra khối `with`       |

Ngoài ra còn rất nhiều special methods khác giúp bạn điều khiển các hành vi nâng cao như toán tử gán cộng (`__iadd__`), toán tử bitwise, quản lý thuộc tính (`__getattr__`, `__setattr__`).

### Different between special methods and normal methods
Sự khác biệt giữa việc định nghĩa **special method** như `__len__` và định nghĩa một hàm bình thường như `count_length()` trong class.

## 1. Sự khác biệt cơ bản

| Điểm khác biệt                  | `__len__(self)` (special method)              | `count_length(self)` (hàm bình thường)          |
|-------------------------------|-----------------------------------------------|-------------------------------------------------|
| Cách gọi                      | Được gọi tự động khi dùng `len(obj)`           | Phải gọi trực tiếp: `obj.count_length()`        |
| Tính tương thích với Python   | Tích hợp với cú pháp và hàm built-in của Python | Không tích hợp, chỉ gọi được như hàm bình thường|
| Tính chuẩn mực của OOP         | Tuân theo chuẩn Python, giúp đối tượng "giống" kiểu dữ liệu chuẩn | Chỉ là phương thức riêng, không chuẩn hóa hành vi|
| Tính mở rộng và tương tác     | Cho phép đối tượng hoạt động mượt mà với các hàm, cấu trúc Python khác | Hạn chế, không tự tương tác với các hàm built-in |

## 2. Ví dụ minh họa

```python
class MyList:
    def __init__(self, elements):
        self.elements = elements

    def __len__(self):
        return len(self.elements)

    def count_length(self):
        return len(self.elements)

my_list = MyList([1, 2, 3])

print(len(my_list))            # Gọi __len__ -> Output: 3
print(my_list.count_length())  # Gọi hàm bình thường -> Output: 3
```

Ở đây, `len(my_list)` sẽ gọi tới `my_list.__len__()` **tự động**. Còn `count_length()` thì phải gọi thủ công.

## 3. Tại sao nên dùng special methods?

- Giúp đối tượng của bạn **tương thích với các tính năng chuẩn của Python** (ví dụ: `len()`, `str()`, toán tử `+`, `-`, `in`, `for`, v.v).
- Khi bạn dùng special methods, bạn có thể làm cho đối tượng của mình hoạt động giống như các kiểu dữ liệu chuẩn (list, dict, str, ...).
- Giúp code của bạn **dễ đọc, dễ hiểu** với những người Python khác, vì họ biết cách sử dụng các tính năng chuẩn.
- Hỗ trợ các thư viện bên ngoài hoặc framework sử dụng các special methods để tương tác với đối tượng của bạn.

### Tóm lại:

- `__len__` giúp bạn dùng được `len(obj)` thay vì phải gọi `obj.count_length()`.
- Đây là cách Python thiết kế để các đối tượng tùy chỉnh vẫn có thể hoạt động mượt mà với cú pháp và hàm built-in.

Nếu bạn muốn, mình có thể giúp bạn viết thêm ví dụ về các special methods khác hoặc cách tận dụng chúng hiệu quả nhé!

# Demonstrate special methods and built-in function corresponding
Dưới đây là **bảng minh họa một số special methods trong Python và các built-in functions tương ứng** mà chúng ta thường dùng, giúp bạn dễ hình dung cách special methods liên kết trực tiếp với các hàm tích hợp của Python:

| Special Method       | Built-in Function / Cú pháp liên quan       | Mô tả ngắn gọn                                   |
|---------------------|---------------------------------------------|-------------------------------------------------|
| `__len__(self)`       | `len(obj)`                                  | Trả về độ dài của đối tượng                      |
| `__str__(self)`       | `str(obj)` hoặc `print(obj)`                 | Trả về chuỗi biểu diễn thân thiện của đối tượng |
| `__repr__(self)`      | `repr(obj)`                                 | Trả về chuỗi biểu diễn chính xác, dùng debug    |
| `__add__(self, other)`| Toán tử `obj1 + obj2`                        | Định nghĩa phép cộng cho đối tượng               |
| `__sub__(self, other)`| Toán tử `obj1 - obj2`                        | Định nghĩa phép trừ cho đối tượng                |
| `__mul__(self, other)`| Toán tử `obj1 * obj2`                        | Định nghĩa phép nhân cho đối tượng               |
| `__truediv__(self, other)`| Toán tử `obj1 / obj2`                    | Định nghĩa phép chia thực cho đối tượng          |
| `__getitem__(self, key)`| `obj[key]`                                | Truy cập phần tử theo chỉ số hoặc khóa            |
| `__setitem__(self, key, value)`| `obj[key] = value`                   | Gán giá trị cho phần tử theo chỉ số hoặc khóa     |
| `__contains__(self, item)`| `item in obj`                            | Kiểm tra phần tử có trong đối tượng hay không    |
| `__iter__(self)`       | Dùng trong vòng lặp `for x in obj`           | Trả về iterator của đối tượng                     |
| `__next__(self)`       | Dùng để lấy phần tử tiếp theo trong iterator | Gọi khi dùng `next(obj)`                          |
| `__call__(self, ...)`  | Gọi đối tượng như hàm: `obj()`               | Cho phép đối tượng được gọi như hàm              |

### Ví dụ liên hệ special method và built-in function:

- `len(obj)` gọi `obj.__len__()`
- `str(obj)` gọi `obj.__str__()`
- `repr(obj)` gọi `obj.__repr__()`
- `obj1 + obj2` gọi `obj1.__add__(obj2)`
- `obj[key]` gọi `obj.__getitem__(key)`
- `item in obj` gọi `obj.__contains__(item)`
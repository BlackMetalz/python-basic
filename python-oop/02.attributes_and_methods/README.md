# 01.class_attributes_and_instance_attributes
- Instance có thể tự thêm mới attributes kể cả khi Class không define.
- Attribute đó chỉ thuộc về riêng instance đó, không chung cho các instance khác.
- Nếu cả class và instance đều có attributes được define thì tất nhiên là sẽ lấy attributes của instance rồi.

# 02.self_parameters
- có thể hiểu self giống như từ "bản thân" trong tiếng Việt, dùng để chỉ chính object đó.
- self có vẻ là 1 dạng parameter mặc định được pass vào instance.
```python
class Person:
    def greet(self):
        print("Hello from", self)

p = Person()
p.greet()  # Python gọi thực chất: Person.greet(p)
```
- self là tham số mặc định đầu tiên trong method, nhận instance hiện tại được truyền vào khi method được gọi.
- Nó được dùng để truy cập thuộc tính và phương thức của chính instance đó.
- Bạn không phải truyền vào self khi gọi method, Python làm việc đó tự động.


# 03.static_methods_and_instance_methods
- Nhìn ví dụ cho dễ hiểu:
```python
class Abc:
    def set_name(self):
        self.name = "kienlt"  # Instance attribute
    
    @staticmethod
    def welcome_msg():
        return "Welcome to the class Abc!"

a = Abc()
a.set_name()
print(a.name)  # Output: kienlt
print(Abc.welcome_msg())  # Call static method without instance
```

# 04.init_method - create a fully initilised object
- Special method trong python bắt đầu với: `__` và kết thúc cũng tương tự, ví dụ `__init__(self)`
- special method init thì hiểu đơn giản là gọi class ra cái thì các attributes đã được set sẵn rồi, và set thông qua special method init.
```python
class Employee:
    def __init__(self, name): # Thêm tham số name
        self.name = name # Gán giá trị parameter name cho attribute self.name

abc = Employee("Kienlt")      # Tạo instance, truyền "Kienlt" làm giá trị cho name
print(abc.name)               # In ra "Kienlt"
```

# 05.conclusion
- Method là 1 function trong 1 class có thể access được toàn bộ attributes của class và xử lý task cụ thể.
- Class attributes là biến dùng chung cho toàn bộ các instance, sửa trên class hoặc một số instance có thể thay đổi chung.
- Sửa lớp attributes qua instance thường tạo instance attribute riêng biệt, không ảnh hưởng class và các instance khác.
```python
class Server:
    provider = "Vietnix"   # class attribute chia sẻ chung
    location = "Vietnam"   # class attribute chia sẻ chung

# Tạo các instance
sv1 = Server()
sv2 = Server()

# Các instance truy cập class attribute
print(sv1.provider)  # Output: Vietnix
print(sv2.location)  # Output: Vietnam

# Thay đổi class attribute qua class
Server.provider = "NewProvider"

# Thay đổi ảnh hưởng đến tất cả instance chưa ghi đè
print(sv1.provider)  # Output: NewProvider
print(sv2.provider)  # Output: NewProvider

# Ví dụ thực tế: ghi lại số lượng Server được tạo
class Server:
    count = 0  # class attribute đếm số lượng instance

    def __init__(self):
        Server.count += 1

s1 = Server()
s2 = Server()
s3 = Server()

print(Server.count)  # Output: 3 - đếm số Server đã tạo
```
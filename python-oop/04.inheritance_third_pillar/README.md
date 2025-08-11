### Single Inheritance
- Powered by Gemini
-  Về cơ bản, class con sẽ "thừa hưởng" được hết các "năng lực" (method) của class cha.
- Trong lập trình, mối quan hệ này thường được ví như quan hệ Cha-Con (Parent-Child). Class kế thừa được gọi là class con (Child Class), và class được kế thừa gọi là class cha (Parent Class).


### Multiple inheritance
- Xem ví dụ ở file 02
- Về cơ bản thi là được thừa hưởng từ nhiều parent class thay vì 1 class, kiểu học võ từ nhiều sư phụ chứ ko phải 1 sư phu như ở single inheritance.

### Multi Level inheritance
- Xem ví dụ ở file 03
- Cái này thì là thừa hưởng từ đời ông tới đời cha rồi đời cháu
```python
class Grandfather:
    def __init__(self):
        self.profession = "Farmer"

    def get_profession(self):
        return f"I am a {self.profession}"

class Father(Grandfather):
    def __init__(self):
        super().__init__()  # Gọi __init__ của Grandfather để lấy profession
        self.profession = "Guard"  # Ghi đè profession

class Child(Father):
    def __init__(self):
        super().__init__()  # Gọi __init__ của Father
        self.profession = "Software Engineer"  # Ghi đè profession

# Thử nghiệm
grandfather = Grandfather()
father = Father()
child = Child()

print(grandfather.get_profession())  # Output: I am a Farmer
print(father.get_profession())       # Output: I am a Guard
print(child.get_profession())        # Output: I am a Software Engineer

```

- Ví dụ khác hay hơn: với ví dụ này thì khởi tạo ra class mới thì vẫn kế thừa được các thuộc tính của nghề nghiệp. Không phải kế thừa trực tiếp thuộc tính của nghề nghiệp, mà Grandfather có một nghề nghiệp làm thuộc tính. Class con kế thừa Grandfather sẽ có thuộc tính nghề nghiệp này.
```python
class Profession:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Grandfather:
    def __init__(self):
        self.profession = Profession("Farmer", 50000)
```

-  Nâng cao hơn là dùng super(), cái này tạm ghi lại chứ ko thực sự là hiểu ở thời điểm này
```python
class Grandfather:
    def __init__(self):
        self.profession = "Farmer"

class Father(Grandfather):
    def __init__(self):
        super().__init__()  # Gọi __init__ của Grandfather để set profession
        self.profession = "Guard"  # Ghi đè profession

father = Father()
print(father.profession)  # Output: Guard
```

### Public, Protected and Private - Naming Conventions in Python
- Public => `member_name`
- Protected => `_member_name` ( 1 underscore)
- Private => `__member_name` ( 2 underscore)
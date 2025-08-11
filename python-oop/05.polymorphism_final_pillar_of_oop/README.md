### Polymorphism
- They may look the same, but their's behaviour are not look the same?
- Cho phép thay đổi behaviour của base class method với derived class?, nghĩa là bạn có thể có method trùng tên với base class.
- Super(). Hmm, hơi khó giải thích. Kiểu như là cho phép gọi lại attribute của parent class từ child class mà không cần phải define lại.

### The Diamond Shape Problem in Multiple Inheritance
- Với ví dụ ở file số 2 thì method sẽ override class đứng trước, trong trường hợp kế thừa từ 2 class như: class D(B,C) thì method trùng tên sẽ được override ở class B thay vì C, do B được define trước C

### Overloading an Operator
- Có vẻ overload phép cộng trừ nhân chia bằng special_method, với cộng thì ta có `__add__` , `__sub__` cho trừ (-), `__mul__` cho nhân (*), `__truediv__` cho chia (/)


### Implementing an Abstract Base Class (ABC)

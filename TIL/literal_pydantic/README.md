Literal trong Pydantic là một kiểu dữ liệu để chỉ định rằng một trường (field) trong model chỉ được phép có giá trị nằm trong một tập hợp giá trị cố định, cụ thể.

Cách sử dụng:
Khi khai báo kiểu trường, dùng Literal[...] với danh sách các giá trị hợp lệ bên trong, ví dụ:

```python
from typing import Literal
from pydantic import BaseModel

class Response(BaseModel):
    status: Literal["success", "failed"]
```

Ý nghĩa là trường status chỉ được phép nhận hai giá trị "success" hoặc "failed". Nếu khi tạo đối tượng mà giá trị khác như "other" được gán cho status thì Pydantic sẽ raise ValidationError (cụ thể có thể là ValueError) cảnh báo giá trị không hợp lệ.

Như vậy Literal rất hữu ích để ràng buộc kiểu trường chỉ có thể có một trong số giá trị cố định được định nghĩa trước mà không cần viết validator thủ công.


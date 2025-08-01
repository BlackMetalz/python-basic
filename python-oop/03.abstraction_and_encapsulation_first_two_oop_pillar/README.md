- Abstraction (Trừu tượng): là khái niệm tập trung vào việc ẩn đi các chi tiết phức tạp bên trong và chỉ cung cấp những chức năng cần thiết cho người dùng. Nó giúp người dùng (hoặc lập trình viên) chỉ cần biết "làm gì" chứ không cần biết "làm như thế nào".

- Encapsulation (Đóng gói): là việc bảo vệ dữ liệu và các chi tiết cài đặt bên trong đối tượng bằng cách đóng gói chúng và chỉ cho phép truy cập qua các phương thức được định nghĩa. Đây là cách để kiểm soát việc tương tác với dữ liệu và bảo vệ dữ liệu không bị thay đổi ngoài ý muốn.


- Ví dụ lái xe ô tô và hành động đạp phanh:
    - Việc lái xe chỉ quan tâm đến hành động đạp phanh mà không cần biết cơ cấu cơ khí hoặc nguyên lý hoạt động bên trong bộ phanh chính là mô hình của abstraction. Bạn thấy được chức năng là "đạp phanh" để xe dừng lại, còn bên trong là hàng loạt cơ chế phức tạp đã được ẩn đi.
    - Encapsulation là chuỗi các xử lý, cơ cấu bên trong hệ thống phanh, được đóng gói lại và không bị lộ ra ngoài cho người lái, đồng thời người lái chỉ có thể tương tác với bộ phanh qua hành động đạp phanh mà thôi. Cơ cấu phanh không bị can thiệp trực tiếp từ bên ngoài, dữ liệu trạng thái và cách xử lý đều được bảo vệ trong bộ phận đó.

Điều này cũng giống như trong lập trình: bạn gọi một method (hàm) của object mà không cần quan tâm cách method đó được thực thi bên trong (abstraction), còn cách object giữ trạng thái thuộc tính private và chỉ thao tác qua getter/setter hoặc method là encapsulation.


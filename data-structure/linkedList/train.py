# Đoàn tàu - Linked List siêu đơn giản

class ToaTau:
    def __init__(self, hang_hoa):
        self.hang_hoa = hang_hoa  # Hàng hóa trong toa
        self.next = None          # Toa tiếp theo
    
    def __str__(self):
        return f"[{self.hang_hoa}]"

class DoanTau:
    def __init__(self):
        self.dau_tau = None  # Toa đầu tiên
    
    def them_toa_cuoi(self, hang_hoa):
        """Thêm toa vào cuối đoàn tàu"""
        toa_moi = ToaTau(hang_hoa)
        
        if not self.dau_tau:  # Chưa có toa nào
            self.dau_tau = toa_moi
            print(f"✅ Đã thêm toa đầu tiên: {toa_moi}")
        else:
            # Tìm toa cuối cùng
            toa_cuoi = self.dau_tau
            while toa_cuoi.next:
                toa_cuoi = toa_cuoi.next
            
            # Nối toa mới vào cuối
            toa_cuoi.next = toa_moi
            print(f"✅ Đã thêm toa cuối: {toa_moi}")
    
    def xem_doan_tau(self):
        """Xem toàn bộ đoàn tàu"""
        if not self.dau_tau:
            print("🚂 Đoàn tàu rỗng")
            return
        
        print("🚂 Đoàn tàu:", end=" ")
        toa_hien_tai = self.dau_tau
        
        while toa_hien_tai:
            print(toa_hien_tai, end="")
            if toa_hien_tai.next:
                print("---", end="")  # Nối giữa các toa
            toa_hien_tai = toa_hien_tai.next
        print()  # Xuống dòng
    
    def dem_toa(self):
        """Đếm số toa"""
        count = 0
        toa_hien_tai = self.dau_tau
        
        while toa_hien_tai:
            count += 1
            toa_hien_tai = toa_hien_tai.next
        
        return count

# Demo đơn giản
def demo():
    print("=== ĐOÀN TÀU (Linked List) ===\n")
    
    # Tạo đoàn tàu rỗng
    doan_tau = DoanTau()
    doan_tau.xem_doan_tau()
    print()
    
    # Thêm các toa
    print("📦 Thêm hàng hóa...")
    doan_tau.them_toa_cuoi("Gạo")
    doan_tau.xem_doan_tau()
    print()
    
    doan_tau.them_toa_cuoi("Thịt")
    doan_tau.xem_doan_tau()
    print()
    
    doan_tau.them_toa_cuoi("Cá")
    doan_tau.xem_doan_tau()
    print()
    
    print(f"📊 Tổng cộng: {doan_tau.dem_toa()} toa")
    print()
    
    # Giải thích
    print("🧠 GIẢI THÍCH:")
    print("- Mỗi toa chỉ biết toa tiếp theo")
    print("- Toa [Gạo] biết toa [Thịt] đứng sau")
    print("- Toa [Thịt] biết toa [Cá] đứng sau")
    print("- Toa [Cá] không biết ai đứng sau (next = None)")
    print()
    print("🎯 Giống như xâu chuỗi, mỗi mắt xích nối với mắt xích tiếp theo!")

if __name__ == "__main__":
    demo()
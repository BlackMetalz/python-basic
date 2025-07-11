# Playlist Music Player sử dụng Linked List

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None  # Bài hát tiếp theo
    
    def __str__(self):
        return f"{self.title} - {self.artist}"

class Playlist:
    def __init__(self):
        self.head = None      # Bài hát đầu tiên
        self.current = None   # Bài hát đang phát
    
    def add_song(self, title, artist):
        """Thêm bài hát vào cuối playlist"""
        new_song = Song(title, artist)
        
        if not self.head:  # Playlist rỗng
            self.head = new_song
            self.current = new_song
        else:
            # Tìm bài cuối cùng
            last_song = self.head
            while last_song.next:
                last_song = last_song.next
            last_song.next = new_song
    
    def play_current(self):
        """Phát bài hiện tại"""
        if self.current:
            return f"🎵 Đang phát: {self.current}"
        return "❌ Không có bài hát nào"
    
    def next_song(self):
        """Chuyển sang bài tiếp theo"""
        if self.current and self.current.next:
            self.current = self.current.next
            return f"⏭️ Chuyển sang: {self.current}"
        return "❌ Đã hết playlist"
    
    def add_after_current(self, title, artist):
        """Thêm bài hát ngay sau bài đang phát (đây là ưu điểm của linked list!)"""
        if not self.current:
            return "❌ Chưa có bài hát nào đang phát"
        
        new_song = Song(title, artist)
        new_song.next = self.current.next  # Nối với bài tiếp theo
        self.current.next = new_song       # Nối bài hiện tại với bài mới
        return f"✅ Đã thêm '{new_song}' vào sau bài đang phát"
    
    def show_playlist(self):
        """Hiển thị toàn bộ playlist"""
        if not self.head:
            return "📝 Playlist rỗng"
        
        songs = []
        current = self.head
        index = 1
        
        while current:
            marker = "🎵" if current == self.current else "  "
            songs.append(f"{marker} {index}. {current}")
            current = current.next
            index += 1
        
        return "📝 Playlist:\n" + "\n".join(songs)

# Demo sử dụng
def demo():
    print("=== MUSIC PLAYER với LINKED LIST ===\n")
    
    # Tạo playlist
    playlist = Playlist()
    
    # Thêm vài bài hát
    print("📁 Thêm bài hát vào playlist...")
    playlist.add_song("See You Again", "Wiz Khalifa")
    playlist.add_song("Despacito", "Luis Fonsi")
    playlist.add_song("Shape of You", "Ed Sheeran")
    
    print(playlist.show_playlist())
    print()
    
    # Phát nhạc
    print(playlist.play_current())
    print()
    
    # Chuyển bài
    print(playlist.next_song())
    print(playlist.show_playlist())
    print()
    
    # Đây là ưu điểm của linked list: thêm bài vào giữa rất nhanh!
    print("🎯 Thêm bài hát ngay sau bài đang phát (O(1) time)...")
    print(playlist.add_after_current("Perfect", "Ed Sheeran"))
    print()
    
    print(playlist.show_playlist())
    print()
    
    # Tiếp tục phát
    print(playlist.next_song())
    print(playlist.next_song())

if __name__ == "__main__":
    demo()
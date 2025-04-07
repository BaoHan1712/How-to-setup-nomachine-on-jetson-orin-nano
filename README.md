  <h2>🚀 Hướng dẫn cài đặt NoMachine trên Jetson Orin Nano</h2>

  <p>Bạn có thể sử dụng NoMachine để điều khiển Jetson Orin Nano từ xa một cách dễ dàng và mượt mà. Hãy làm theo các bước sau:</p>

  <pre>
# Bước 1: Tải file cài đặt NoMachine cho ARM64
wget https://www.nomachine.com/free/arm/v8/deb -O nomachine.deb

# Bước 2: Cài đặt gói DEB
sudo dpkg -i nomachine.deb

# Bước 3: Đặt chế độ khởi động không dùng giao diện đồ họa (tùy chọn)
sudo systemctl set-default multi-user.target

# Bước 4: Khởi động lại dịch vụ NoMachine
sudo /usr/NX/bin/nxserver --restart
  </pre>

  <pre> Mở terminal và chạy lệnh sau để cài đặt OpenSSH Server:
   sudo apt update
   sudo apt install openssh-server

Sau khi cài đặt, bạn cần khởi động dịch vụ SSH:
   sudo systemctl start ssh

Để đảm bảo dịch vụ SSH tự động khởi động khi hệ thống khởi động, chạy lệnh sau:
   sudo systemctl enable ssh

Từ máy tính khác, bạn có thể kết nối đến Jetson Orin Nano bằng lệnh SSH. Thay username bằng tên người dùng của bạn và ip_address bằng địa chỉ IP của Jetson Orin Nano:
   ssh username@ip_address
  </pre>

  <h2>💻 Tải NoMachine cho Laptop</h2>
  <p>Truy cập vào trang chủ NoMachine để tải và cài đặt:</p>
  <p><a href="https://www.nomachine.com/" target="_blank">🔗 https://www.nomachine.com/</a></p>

  <p>Chúc bạn kết nối Jetson Orin thành công và mượt mà! 🧠🔧</p>


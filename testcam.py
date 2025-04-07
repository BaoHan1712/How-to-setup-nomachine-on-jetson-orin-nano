import cv2

# Mở camera (0 là camera mặc định, nếu có nhiều camera thì đổi thành 1, 2, ...)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Không thể mở camera")
    exit()

while True:
    # Đọc khung hình từ camera
    ret, frame = cap.read()
    
    if not ret:
        print("Không thể nhận dữ liệu từ camera")
        break

    # Hiển thị hình ảnh
    cv2.imshow("Camera", frame)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()

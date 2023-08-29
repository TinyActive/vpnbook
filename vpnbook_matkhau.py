import easyocr
import requests
import numpy as np
import cv2
import warnings

# Định nghĩa một decorator để tạm thời chuyển cảnh báo về mức "mute"
def suppress_warnings(func):
    def wrapper(*args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            result = func(*args, **kwargs)
        return result
    return wrapper

@suppress_warnings
def run_easyocr(image_url):
    # Khởi tạo một đối tượng EasyOCR với các ngôn ngữ mặc định
    reader = easyocr.Reader(['en'])

    # Tải hình ảnh từ URL và chuyển thành mảng NumPy
    response = requests.get(image_url)
    image_data = np.frombuffer(response.content, np.uint8)
    image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

    # Sử dụng EasyOCR để nhận dạng chữ trong ảnh
    results = reader.readtext(image)

    # Lưu văn bản nhận dạng vào tệp văn bản
    with open('abc.txt', 'w', encoding='utf-8') as f:
        for (bbox, text, prob) in results:
            f.write(f'{text}')

    print("Đã lưu văn bản vào tệp abc.txt")

image_url = 'https://www.vpnbook.com/password.php'
run_easyocr(image_url)

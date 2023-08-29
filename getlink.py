import requests
from bs4 import BeautifulSoup
import re

# URL của trang web cần crawl
url = 'https://www.vpnbook.com/'

# Gửi yêu cầu GET đến trang web và lấy nội dung
response = requests.get(url)
html_content = response.text

# Sử dụng BeautifulSoup để phân tích cú pháp HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Tìm tất cả các thẻ <a> chứa liên kết
links = soup.find_all('a')

# Biểu thức chính quy để tìm các liên kết đến tập tin zip
zip_link_pattern = re.compile(r'.*\.zip$')

# Lưu trữ các liên kết tập tin zip đã tìm thấy
zip_links = []

# Lọc và lưu trữ các liên kết tập tin zip
for link in links:
    href = link.get('href')
    if href and re.match(zip_link_pattern, href):
        zip_links.append(href)

# In ra danh sách các liên kết tập tin zip
for zip_link in zip_links:
    print(f'https://www.vpnbook.com{zip_link}')

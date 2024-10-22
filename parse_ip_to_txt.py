import requests
from bs4 import BeautifulSoup

url = 'https://mail.ru'  # замените на URL вашей страницы
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
ip_addresses = []

for ip_tag in soup.select('td:nth-child(1)'):
    ip_addresses.append(ip_tag.text)
for ip in ip_addresses:
    print(ip)

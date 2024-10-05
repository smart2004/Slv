import webbrowser
import os
from dotenv import load_dotenv


load_dotenv()
# SECRET_KEY = os.getenv('SECRET_KEY')
api_key = os.getenv('key')
file = open(r"ids.txt", "r")
ids = []
lines = file.readlines()

count = 0
for line in lines:
    ids.append(line.strip())

try:
    for one in ids:
        try:
            url = f'https://api.ip2location.io/?key={api_key}&ip={one}'
            webbrowser.open(url)
            count += 1

            url1 = f'https://www.geolocation.com/?ip={one}#ipresult'
            webbrowser.open(url1)
        
        except Exception as e:
            print(f"An error occurred for id {one}: {str(e)}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

print("Sent qty: ", count)

file.close()

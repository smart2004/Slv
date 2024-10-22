from datetime import datetime
import xlwt
import webbrowser, requests

api_key = key = '75FD...'
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

            data = requests.get(url).json()


            url1 = f'https://www.geolocation.com/?ip={one}#ipresult'
            webbrowser.open(url1)

        except Exception as e:
            print(f"An error occurred for id {one}: {str(e)}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

print("Sent qty: ", count)

file.close()


wb = xlwt.Workbook()
ws = wb.add_sheet("Site visitors")
# style1 = xlwt(num_format_str='DD-MM-YY')
style1 = xlwt.XFStyle()
style1.num_format_str = 'DD-MM-YY'

ws.write(1, 1, 'Today is:')
ws.write(1, 2, datetime.now(), style1)
ip = "and I'm a King :)"
text_length = len(text)
ws.write(1, 3, text)

wb.save('FVV.xls')

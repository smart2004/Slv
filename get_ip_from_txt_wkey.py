import webbrowser

api_key = key = '75FDA9745EBE1B1E5A6E35D6F9E40D38'
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

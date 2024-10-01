file = open(r"ids.txt", "r")
ids = []
lines = file.readlines()

count = 0
for line in lines:
    ids.append(line.strip())

try:
    for one in ids:
        try:
            getattr # think on request for geo-API
            count += 1
        except Exception as e:
            print(f"An error occurred for id {one}: {str(e)}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

print("Sent qty: ", count)

file.close()

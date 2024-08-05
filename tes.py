import requests

url = "https://raw.githubusercontent.com/Michele0303/tiktok-live-recorder/main/src/utils/enums.py"
test = requests.get(url)
data: str = test.text

for line in data.split("\n"):
    # if 'class' in line:
    #     print(line)
    #     break
    if "VERSION" in line:
        version = line.split("=")[1].strip()
        print(version)
        # print(line.strip())
        break

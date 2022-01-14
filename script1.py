import requests
result = requests.get("https://raw.githubusercontent.com/v6k/CMPUT404LAB1/main/script1.py")
print(result.text)

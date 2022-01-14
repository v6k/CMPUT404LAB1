import requests
result = requests.get("https://github.com/v6k/CMPUT404LAB1/blob/main/script1.py")
print(result.status_code)

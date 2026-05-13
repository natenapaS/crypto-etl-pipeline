import requests

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {"vs_currency": "usd", "ids": "bitcoin"}
headers = {"User-Agent": "Mozilla/5.0"}

print("Sending request...")
response = requests.get(url, params=params, headers=headers, timeout=5, verify=False)
print(f"Status: {response.status_code}")
print(response.json()[0]["current_price"])
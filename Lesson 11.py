import requests

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for currency in data:
        if currency["r030"] == 840:
            print(f"USD - {currency['rate']} грн")

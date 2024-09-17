import requests
import json

# URL и заголовки
url_sales_funnel_summary =
headers = {}

# Тело запроса
payload = {
    "start": "2024-09-10",
    "end": "2024-09-16",
    "aggregationLevel": "day",
    "nmIDs": [],
    "subjectIDs": [],
    "brandNames": [],
    "tags": [],
    "skipDeletedNm": False,
    "stockType": ""
}

# Отладочная информация
print("URL:", url_sales_funnel_summary)
print("Headers:", headers)
print("Payload:", json.dumps(payload, indent=2))

# Отправка запроса
response = requests.post(url_sales_funnel_summary, headers=headers, json=payload)

# Вывод ответа и статуса
print("Status Code:", response.status_code)
print("Response Text:", response.text)
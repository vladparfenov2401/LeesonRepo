import requests
import json

# URL и заголовки
url_sales_funnel_summary = 'https://seller-content.wildberries.ru/ns/analytics-api/content-analytics/api/v1/sales-funnel/report'
headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,zh;q=0.6,zh-TW;q=0.5,zh-HK;q=0.4,zh-CN;q=0.3',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'cookie': '_wbauid=10153997811724154298; wbx-validation-key=cb4540fc-45c5-47fc-9294-3190b1cb4dc8; ___wbu=f70a2932-edc7-4340-80d9-badb44fa2453.1724236958; WBTokenV3=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MjQ5MzQ1NjMsInZlcnNpb24iOjIsInVzZXIiOiIxNzA5NDA0NSIsInNoYXJkX2tleSI6IjEwIiwiY2xpZW50X2lkIjoic2VsbGVyLXBvcnRhbCIsInNlc3Npb25faWQiOiI0MmNmMjQwMDU1ZDI0YWQzYTEzOWQ3ZTFjM2Y0ODNiYiIsInVzZXJfcmVnaXN0cmF0aW9uX2R0IjoxNjc0MDQ1NTY3LCJ2YWxpZGF0aW9uX2tleSI6IjBkZDM3YzNhZDc1NWUxOTk0ZDMyZDlkNTlhZjZhZGIzZjFkNGNjNGEwZDE4YzJkZjJjMjc2N2RmYTcyMGMxMjgiLCJwaG9uZSI6IiJ9.Lpe41Be6eGjiSg_ZJlIAw6fbWcUZqwEu_bn3TG8Q32nitsJOZ_obcwGaF52a8Y88yk26oAEx4efp-60HLMXiiUrZ0bNz9hvzv3_BKSJ1Uz6VDLVS3rUPia-_ke2y95LuR4a0Rn-SWv-IDrEEfBb_VN1nLQ3cUyoiaUlKcQrXN_4pDIocsTyYt_h16CrH8t1TO_TH4qLDKrwRotw7geyRMJEv1uiT95AFwRZuIXGO_-kOVdua-wf2K6r-8YFEPAYVyYFlGFmn8IgjIoctXCEXQADGJlN_aJsM9rZzMIlhxfR8f70AfDGV5nk4S3PQMQ9bdthIxgWjND7a9WiBIk9Xew; external-locale=ru; __zzatw-wb-t=MDA0dC0cTHtmcDhhDHEWTT17CT4VHThHKHIzd2UvQ2wdZUhhET9HFTZnXEpCNxVZcU4nfAsmMl4tYQ8rCB5UNV9OCCcfFQhzKlEJEF9CPV8/cnsiD2k5IVt0FhNFWmFVaUAfQTY6flJkGBRIWRw2czljajUjfj1qTnsJXSZWCjxdb0F0Ly5zZiFoSVpRTFlPeyhLFDRwJVg8Pl89M2llaXAvYCASJRFNRxhFZFtCNigVS3FPHHp2X30qQmcjY1BhJkVXUn0qFXtDPGMMcRVNfX0mNGd/ImUrOS4bNSIYNmdITT4mVBM8dWUQMzssZQgiD2k5I2Q1UT9BWltUODZnQRF1JgkINyxgcFcZURMaXHhHV3osGxd7dCtWCQ1gQUdpZW0MLVJRUUtffw4OP2lOWUNdcEtxTih9CTE0Xn0cVhs5Y2o1I349ak57CV1ZCQkQFkZ2dnBcbCIlXExbU3VSf38tTg5+bikKCA9hQ3JwMS4tYQ8nfCNifCAZay8LVEMyZQg+QE05Mzk0ZnBXJ2BOWyVHXlUIJxsXeG0fQUtUI3Izd2Vpdx5WJRMWZw9HIk4=5/7Cyw==; cfidsw-wb-t=e9Z1hXLprijlXoZiktbBs38910WGq4avB6ISqR6xaE0vh+6NxrsUOtXrT+pXbOyrozmV5dn8Ex38RBOTgu1R7ffJQDVWOPJOo0n230vd2pZHBoth9eNEOMNBm9lEFVFACoSYW6+zysjYeUhYm58P+1a/IVLHm440hhs+lf6O; x-supplier-id-external=1866b905-1d2b-52eb-90a4-554e3f4f8f52; __zzatw-wb=MDA0dC0cTHtmcDhhDHEWTT17CT4VHThHKHIzd2UqQmUmY0ddJDVRP0FaW1Q4NmdBEXUmCQg3LGBwVxlRExpceEdXeiwbF3xrJFQMDGE/SGllbQwtUlFRS19/Dg4/aU5ZQ11wS3E6EmBWGB5CWgtMeFtLKRZHGzJhXkZpdRVTCT4ZP0Vtcy5AIR9jeBUidFZQClkgRngmJg0LE15vc19vG3siXyoIJGM1Xz9EaVhTMCpYQXt1J3Z+KmUzPGwfZUxZIEhaTn8nIQ1pN2wXPHVlLwkxLGJ5MVIvE0tsP0caRFpbQDsyVghDQE1HFF9BWncyUlFRS2EQR0lrZU5TQixmG3EVTQgNND1aciIPWzklWAgSPwsmIBN9cCNQDBBcQ0N1bxt/Nl0cOWMRCxl+OmNdRkc3FSR7dSYKCTU3YnAvTCB7SykWRxsyYV5GaXUVUA8RYW9KbXgmPCEfGUReIXgPSgolShV0cChTPA4ZQXd1MS49VxlRDxZhDhYYRRcje0I3Yhk4QhgvPV8/YngiD2lIYCFJWk16Kh4Td20sS3FPLH12X30beylOIA0lVBMhP05yzXCnuA==; cfidsw-wb=1+aT9JczN90oWplkFMa7ry+yXbKN+wDid3t4l2Ll0YCmNCN3Bt8B71KunQtzUvhglfgS0Ae+dL9V8tEQDwt/BPmLM7a4KYzZU51uxJr15Its39t2IbB3/0B8cFTuosaWm1KnpUVJ5/MkSEzl0Ywl5ZMJxgwLshZGp/BopEpm',
    'dnt': '1',
    'origin': 'https://seller.wildberries.ru',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://seller.wildberries.ru/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

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
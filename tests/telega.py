import requests
import unittest

class APITest(unittest.TestCase):
    def setUp(self):
}
        self.data = {
            "currentPeriod": {"start": "2024-09-07", "end": "2024-09-13"},
            "subjects": [],
            "brands": [],
            "nms": [],
            "tagIds": [],
            "skipDeletedNm": False,
            "orderBy": {"field": "orders", "mode": "desc"},
            "prevPeriod": {"start": "2024-08-31", "end": "2024-09-06"}
        }

    def test_sales_funnel_report(self):
        response = requests.post(self.url, headers=self.headers, json=self.data)
        self.assertEqual(response.status_code, 200, f"Expected status code 200, but got {response.status_code}")
        # Можно добавить дополнительные проверки здесь, если нужно

if __name__ == '__main__':
    unittest.main()
import requests
import time


res = requests.get("https://zalcademy.ir")
# print(res.text)
# print(res.status_code)

res = requests.get('http://httpbin.org/get')
# print(res)
# print(res.text)
# print(res.json()['headers'])

my_data = {
    "bahman": "09388309605",
    "zal": "546596596"
}
res = requests.post("http://httpbin.org/post", json=my_data)
# print(res)
# print(res.json())

sites = ["https://zalcademy.ir", "https://google.com", "http://zalcademy.ir/fguhisdrfg"]

while True:
    for s in sites:
        print("Checking the address -> " + s)
        try:
            res = requests.get(s)
            if res.status_code != 200:
                data = {
                    "text": s + " Failed with status of " + str(res.status_code)
                }
                r = requests.post('https://hooks.slack.com/services/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', json=data)
        except Exception as e:
            data = {
                    "text": "An exception eccured  " + e
                }
            r = requests.post('https://hooks.slack.com/services/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', json=data)
    time.sleep(30)

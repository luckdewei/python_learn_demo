import requests

while True:
    url = "https://www.baidu.com"

    try:
        res = requests.get(url)
    except Exception as e:
        print(f"请求失败原因：{e}")
        continue

    with open("content.txt", mode="wb") as f:
        f.write(res.content)

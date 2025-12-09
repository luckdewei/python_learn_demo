import requests


url = "http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22"

response = requests.get(url)

print(f"response:{response}")

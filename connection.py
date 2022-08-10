import json
import requests

try:
    data = requests.get('http://localhost:8000/api/stock/stock_obj')
    print(data.text)
except:
    print('error')
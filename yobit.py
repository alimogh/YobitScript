import json
import requests

yobit_id = 'BDE00D8CCD62E3C1166550BE6FBD1AE2'
yobit_hash = b'c28f53d25ef0cb39542e3e642e0eb32b'


link = "https://yobit.net/api/3/ticker/XXX_eth"

XXX= 55


res = requests.get('https://yobit.net/api/3/ticker/ltc_btc') # получаем данные ticker'а
res_obj = json.loads(res.text) # переводим полученный текст в объект с данными

print("SELL: %0.8f" % res_obj['ltc_btc']['sell'])
print("BUY: %0.8f" % res_obj['ltc_btc']['buy'])
print(res_obj)
print(res)
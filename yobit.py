import json
import requests
#verification
yobit_id = 'BDE00D8CCD62E3C1166550BE6FBD1AE2'
yobit_hash = b'c28f53d25ef0cb39542e3e642e0eb32b'

#catch coin!
xxx = "ltc"
txxx = "ltc".upper()
#creating data link
link1 = "https://yobit.net/api/3/ticker/"+xxx+"_eth"
link2 = "https://yobit.net/api/3/ticker/"+xxx+"_btc"
#creating trade link
tlink1 = "https://yobit.net/ru/trade/"+txxx+"/ETH"
#check link
print(link1)
"""
res = requests.get(link1) # получаем данные ticker'а
res_obj = json.loads(res.text) # переводим полученный текст в объект с данными
print("SELL: %0.8f" % res_obj['ltc_eth']['sell'])
print("BUY: %0.8f" % res_obj['ltc_eth']['buy'])
print(res_obj)
print(res)
"""
res = requests.
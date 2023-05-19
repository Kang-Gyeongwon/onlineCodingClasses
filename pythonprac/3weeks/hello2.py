import requests

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

rows = rjson['RealtimeCityAir']['row']

for a in rows:
    # print(a)
    
    gu_name = a['MSRSTE_NM']
    gu_miss = a['IDEX_MVL']
    print(gu_name, gu_miss)
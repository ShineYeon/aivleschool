#magic command에 의해서 아래의 코드가 python코드로 저장이 된다.
#함수에서 사용되는 패키지도 같이 추가해야 한다.

import requests
import pandas as pd
import geohash2

def oneroom(addr) :
    url = f'https://apis.zigbang.com/v2/search?leaseYn=N&q={addr}&serviceType=원룸'
    response = requests.get(url)
    response.json() #우리가 필요한 값은 lat, lng
    data = response.json()["items"][0]
    lat, lng = data["lat"], data["lng"]
    geohash = geohash2.encode(lat, lng, precision=5)
    
    url = f'https://apis.zigbang.com/v2/items?deposit_gteq=0&domain=zigbang\
&geohash={geohash}&needHasNoFiltered=true&rent_gteq=0&sales_type_in=전세|월세&service_type_eq=원룸'
    response = requests.get(url)
    items = response.json()["items"]
    ids = [item["item_id"] for item in items ]
    
    url = 'https://apis.zigbang.com/v2/items/list'
    params = {
    "domain": "zigbang",
    "withCoalition" : "true",
    "item_ids" : ids[:900]
    }
    response = requests.post(url, params)
    items = response.json()["items"]
    columns = ["item_id", "sales_type", "deposit", "rent", "size_m2", "address1", "manage_cost"]
    return pd.DataFrame(items)[columns]
    

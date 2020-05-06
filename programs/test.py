'''from pytube import  YouTube


YouTube('https://www.youtube.com/watch?v=SxTYjptEzZs').streams[0].download()'''



import requests
import json

api_request= requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=d34e2cbd-43ca-435c-9a56-fcfcd8e364cb")
api = json.loads(api_request.content)
print(api['data'][0]['name']) 
print(api['data'][0]['quote']['USD']['price'])

'''data = api['data']
for item in data:
    print(item['name'],item['quote']['USD']['price'])'''
    
for i in range(0,5):
    print(api['data'][i]['symbol'], '{0:.2f}'.format(api['data'][i]['quote']['USD']['price']), sep='-')
    











import requests
import json

category1 = 'Brass Instruments'
category2 = 'Woodwind Instruments'
category3 = 'String Instruments'

# product1 = 'guitar'
# product2 = 'violin'
# product3 = 'saxophone'

product1 = 'violin'
product2 = ''
product3 = ''

minprice1 = 10
minprice2 = 10
minprice3 = 10

maxprice1 = 1500
maxprice2 = 1500
maxprice3 = 2000


data1 = requests.get('http://localhost:8000/api/products?product='+product1+'&category='+category3+'&min-price='+str(minprice1)+'&max-price='+str(maxprice1))

#data2 = requests.get('http://127.0.0.1:8000/api/products?product='+product2+'&category='+category2+'&min-price='+str(minprice2)+'&max-price='+str(maxprice2))

#data3 = requests.get('http://127.0.0.1:8000/api/products?product='+product3+'&category='+category3+'&min-price='+str(minprice3)+'&max-price='+str(maxprice3))

print('>>>>>>>>>>> TEST API 1')
print(data1.json())
#print('>>>>>>>>>>> TEST API 2')
# print(data2.json())
# print('>>>>>>>>>>> TEST API 3')
# print(data3.json())

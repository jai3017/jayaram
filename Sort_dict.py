import requests
url='http://data.fixer.io/api/2017-01-01?access_key=401b813f53bc48488e308cb9a13e06fb'
url2='http://data.fixer.io/api/2018-01-01?access_key=401b813f53bc48488e308cb9a13e06fb'
url1=requests.get(url)
url2=requests.get(url2)
data_2017=url1.json()
data_2018=url2.json()
new_dict={}
for i,j in data_2017['rates'].items():
    for g,h in data_2018['rates'].items():
        if i==g:
            new_dict[i]=float("{:.2f}".format(((h-j)*100)/j))

[print(key,value)  for key,value in sorted(new_dict.items(),key=lambda x:x[1])]

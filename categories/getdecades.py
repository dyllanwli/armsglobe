# pylint-disable 
import json
from collections import defaultdict
with open("/h/diya.li/cidi/armsglobe/categories/newAll.json", "r") as f:
    j = json.load(f)

timebins = j['timebins']
timebins.sort(key = lambda x: x['t'])
dic = defaultdict(lambda : defaultdict(int))

for i in range(len(timebins)):
    decades = timebins[i]['t'][-2]
    if decades != "l":
        decades = str(decades) + "0s"
    else:
        decades = "N/A"
    data = timebins[i]['data']
    for c in data:
        dic[decades][c['e']] += c['v']
        dic["all"][c['e']] += c['v']


output = {'timeBins': []}

for years in dic:
    # print(dic[years])
    datalist = []
    for country in dic[years]:
        data = {"i": "United States","wc": "mil","e": country,"v": dic[years][country]}
        datalist.append(data)
    
    output['timeBins'].append({'data': datalist, 't':years})
# print(output)
with open("./newnew.json", "w") as f:
    json.dump(output, f)
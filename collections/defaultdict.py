from collections import defaultdict,Counter,ChainMap
#import OrderDict as OrderDict
'''d1=defaultdict(int)
d2=defaultdict(list)
d1["a"]=1
d1["b"]=2
d2["x"]=[22,3,3,3]
print(d1)
print(d2)
l=[1,2,3,93,1,3,5,2,3,5]
l2=Counter(l)
print(l2)
d={"a":2,"b":1}
o=OrderDict()
o["a"]=1
o["b"]=2
o["c"]=3
for k,v in o.items():
    print(k,v)'''
dict1={"a":10,"b":20}
dict2={"x":20,"y":37}
dt=ChainMap(dict1,dict2)
print(dt)


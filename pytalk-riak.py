__author__ = 'darko.ronic'

# Connecting to a Riak cluster

import riak
n = riak.RiakNode(host="192.168.59.103", http_port=8098, pb_port=8087)
r = riak.RiakClient(protocol="pbc", nodes=[n])
print r

# Using a bucket

b = r.bucket("pytalk.bucket.test")
print b

# storing a key/value

data = {"mainId": "firstKey", "city": "Zagreb", "country": "Mongolia", "postnumber": 29457}
o = b.new(key="thisIsTheFirstKey", data=data)
print o.store()

# fetching object

o = b.get("thisIsTheFirstKey")
print o.exists
print o.data

# changing object

o.data["country"] = "Japan"
o.data["continent"] = "Africa"
print o.store()

# deleting object

o.delete()
b.delete("thisIsTheFirstKey")
print b.get("thisIsTheFirstKey").exists

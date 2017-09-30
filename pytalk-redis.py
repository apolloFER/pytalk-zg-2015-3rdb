__author__ = 'darko.ronic'

# connecting to Redis

import redis
r = redis.StrictRedis(host="192.168.59.103", port=5379, db=0)
print r

# basic data type

r.set("pytalk:example:key", "randomvalue")
print r.get("pytalk:example:key")

# set data type

r.sadd("pytalk:example:setkey", "randomvalue1")
r.sadd("pytalk:example:setkey", "anothervalue")
r.sadd("pytalk:example:setkey", "valueagain")
print r.srandmember("pytalk:example:setkey")

# sorted set data type

r.zadd("pytalk:example:sortedsetkey", 45.1, "firstvalue")
r.zadd("pytalk:example:sortedsetkey", 13.4, "myvalue")
r.zadd("pytalk:example:sortedsetkey", 49.2, "enteringvalue")
r.zadd("pytalk:example:sortedsetkey", 33.8, "randommember2")
print r.zrank("pytalk:example:sortedsetkey", "randommember2")
print r.zrange("pytalk:example:sortedsetkey", 0, -1)

# hash data type

r.hset("pytalk:example:hashkey", "aKey", 55.2)
r.hset("pytalk:example:hashkey", "bKey", "randomstring")
r.hset("pytalk:example:hashkey", "cKey", "This is a value")
print r.hgetall("pytalk:example:hashkey")

# list data type

r.rpush("pytalk:example:listkey", "randvalue")
r.lpush("pytalk:example:listkey", "anotherKey")
print r.lpop("pytalk:example:listkey")
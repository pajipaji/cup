#

set server:name "hh"
get server:name
exists server:name
set connections 10
incr connections
del connections
incrby connection 30
decr connection
decrby connection 10

set reource:lock "redis demo"
expire resource:lock 120
ttl resource:lock
set resource:lock "redis demo2"
expire resource:lock 120
ttl resource:lock
set resource:lock "redis demo3"
ttl resource:lock
set resource:lock "redis demo4" ex 5
ttl resource:lock
set resource:lock "redis demo5" ex 10
persist resource:lock
ttl resource:lock => -1

rpush friends "Alan"
rpush friends "bob"
lpush friends "cc"
lrange friends 0 -1
lrange friends 0 1
lrange friends 0 2
lpop friends
rpop friends
llen friends
lrange friends 0 -1
rpush friends 1 2 3
llen friends

sadd superpowers "flight"
sadd superpowers "x-ray vision" "reflexes"
srem superpowers "reflexes"

sismember superpowers "fight"
sismember superpower "reflexes"
smembers superpowers
sadd birdpowers "pecking"
sadd birdpowers "flight"
sunion superpowers birdpowers

sadd letters a b c d e f
spop letters 2
smembers letters

zadd hacker 1940 "a"
zadd hacker 1906 "g
zadd hacker 1953 "r"
zadd hacker 1922 "h"
zrange hacker 2 4

hset user:1000 name "edd"
hset user:1000 email "ikefire@qq.com"
hset user:1000 password "include"
hgetall user:1000
HMSET user:1001 name "Mary Jones" password "hidden" email "mjones@example.com"
HGET user:1001 name

hset user:1000 visits 10
hincrby user:1000 visits 1
hincrby user:1000 visits 10
hdel user:1000 visits
hincrby user:1000 visits 1


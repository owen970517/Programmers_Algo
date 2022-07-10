from functools import cache


def solution(cacheSize, cities):
    answer = 0
    cache=[]
    upper = []
    for i in cities :
        upper.append(i.upper())
    for city in upper:
        if not city in cache:
            if len(cache) < cacheSize :
                cache.append(city)
                answer+=5
            elif cacheSize == 0 :
                answer += 5
            else :
                cache.pop(0)
                cache.append(city)
                answer +=5
        else :
            cache.pop(cache.index(city))
            cache.append(city)
            answer += 1
    return answer

cacheSize = 0
cities = 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize,cities))


""" #LRU 알고리즘
cacheSize = 3
reference = ['a','b','a']
upper = []
for i in reference :
  upper.append(i.upper())
cache = []
time = 0
for ref in upper:
  if not ref in cache:
    # cache miss 인 경우
    if len(cache) <= cacheSize:
        cache.append(ref)
        time+=5
    else:
        cache.pop(0)
        cache.append(ref)
        time += 5
  # cache hit 인 경우 
  else:
      cache.pop(cache.index(ref))
      cache.append(ref) 
      time += 1

print(cache,time) """
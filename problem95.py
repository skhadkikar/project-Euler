import json

def divisor(num):
    divs = [1]
    i = 2
    while i**2 <= num:
        if i**2 == num:
            divs.append(i)
        elif num % i == 0:
            divs.append(i)
            divs.append(num//i)
        i += 1
    divs.sort()
    return divs

def sum(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

def cycle_detect(g, v):
    tortoise = v
    hare = g[str(v)]
    while tortoise != hare:
        if hare < 1000000 and g[str(hare)] < 1000000: # if hare doesn't hit a dead end
            tortoise = g[str(tortoise)]
            hare = g[str(g[str(hare)])]
        else: 
            return None 
    if g[str(tortoise)] != tortoise and g[str(tortoise)] < 1000000: # if not a dead end, return cycle
        return tortoise             
    else: # else return not a cycle
        return None

# max = 1000000
# facs = dict()
# for i in range(max):
#     facs[i] = sum(divisor(i))
# with open('proper_divisors_sum.txt','w') as f:
#     f.write(json.dumps(facs))

with open('proper_divisors_sum.txt','r') as f:
    data = f.read()
graph = json.loads(data)
cyclical = set()
print('preprocessing done')

for v in range(1000000):
    # print(v)
    if v in cyclical: # if cycle or lack thereof already detected
        continue
    node = cycle_detect(graph,v)
    if node in cyclical: # if cycle or lack thereof already detected
        continue
    if node is not None:
        init = node
        while graph[str(node)] != init:
            print(node,end=" -> ")
            cyclical.add(node)
            node = graph[str(node)]
        cyclical.add(node)
        print(node,end=" -> ")
        print(init)
    else:
        node = v
        while node in graph and node != graph[str(node)]:
            cyclical.add(node)
            node = graph[str(node)]


import math

cals_in_bottle = 400

cases = int(input())

reqs = []

for i in range(cases):

    req = int(input())
    reqs.append(req)

for req in reqs:

    print(math.ceil(req/cals_in_bottle))
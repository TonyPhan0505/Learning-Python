# 1. Generate pairs of arrays lengths
# 2. For each pair, generate two containers with appropriate samples.
# 3. Loop through the two containers, check if an item from a container matches one in the other. If one valid match is found, return True.
# 4. Return False.

import math

import random

def splitArray(nums):
    
    z = math.floor(len(nums)/2) + 1
    
    def average(a):
    
        return sum(a)/len(a)

    for w in range(1, z):

        m = len(nums) - w

        c1 = []

        c2 = []

        nc1 = math.factorial(len(nums))/(math.factorial(w) * math.factorial(len(nums) - w))

        nc2 = math.factorial(len(nums))/(math.factorial(m) * math.factorial(len(nums) - m))

        while len(c1) < nc1:

            item1 = set(random.sample(nums, w))

            if item1 not in c1:

                c1.append(item1)

        while len(c2) < nc2:

            item2 = set(random.sample(nums, m))

            if item2 not in c2:

                c2.append(item2)

        for i in c1:

            for j in c2:

                condition = not any(q for q in i if q in j)

                if average(i) == average(j) and condition:

                    return True

    return False

print(splitArray([1,2,3,4,5,6,7,8]))

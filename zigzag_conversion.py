# Select letters that will stand in the middle. Put them in a list. Call this list m.
# Select substrings on the vertical lines. Put them in a list. Call this list v.

import numpy as np

from functools import reduce

def zigzagConversion(s, n):
    
    if n == 1:
    
        return s

    # Select middle letters

    s = [c for c in s]
    
    t = n - 2

    p = n

    m = []

    mps = []

    while p < len(s) - 1:

        for i in range(t):

            m.append(s[p])

            mps.append(p)

            p += 1

        p += n

    m = [list(i) for i in np.array_split(m, len(m)/t)]

    for l in m:

        r = -2

        for i in range(len(l)):

            p = [' '] * n

            if r <= -(len(l)-1):

                p[r] = l[i]

                l[i] = p

                r -= 1
    
    m = reduce(lambda x, y: x + y, m)

    # Select vertical substrings

    a = [s[i] for i in range(len(s)) if i not in mps]

    v = []

    r = a[-(len(a)%n):]  

    a = a[0:-(len(a)%n)]

    vs = np.array_split(a, len(a)/n)

    v = [list(i) for i in vs]

    v.append(r)

    # Combine verticals and middles in the right order

    if (len(s) - len(v[-1])) % (n+t) == 0:

        missing = [' '] * (n - len(v[-1]))

        v[-1] = v[-1] + missing

    else:

        for i in range(len(v[-1])):

            r = -2

            p = [' '] * n

            p[r] = v[-1][i]

            v[-1][i] = ''.join(p)

            r -= 1

    r = 1

    for i in m:

        v.insert(r, i)

        if (r+1)%(t+1) != 0:
            
            r += 1

        else:

            r += 2

    s = ''

    r = 0
    
    while r < n:

        for i in v:

            s += i[r]

        r += 1

    return s.replace(' ','')

print(zigzagConversion('PAYPALISHIRING', 4))



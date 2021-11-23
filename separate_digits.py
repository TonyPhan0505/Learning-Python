# 1. Insert ccommas into the string
# 2. All commas move to the right. The comma on the very right moves first, then the next comma and so on.
# 3. Each time a comma moves, record the sequence in a container.
# 4. Filter the container to only contain sequences in ascending order.

def numberOfCombinations(n):
    
    # Check if an array is in ascending order.

    def isInAscendingOrder(a):
    
        flag = 0
    
        r = 1
    
        while r < len(a):
    
            if a[r] < a[r-1]:

                flag = 1

            r += 1
                
        if not flag:
            
            return False
                
        else:
            
            return True

    # All possible arrays formed with commas
    
    ans = []

    for c in range(1, len(n)):
        
        # Insert commas into the string

        digits = [d for d in n]

        for p in range(1, c*2, 2):

            digits.insert(p, ',')
        
        s = ''.join(digits)

        ans.append(s)

        # Move commas to the right 1 step at a time and record results of the movements.
        
        lcp = c*2-1
        
        while lcp < len(digits) - 2:

            for p in range(int(c*2-1), 0, -2):

                digits[p], digits[p+1] = digits[p+1], digits[p]

                s = ''.join(digits)

                ans.append(s)

            lcp += 1

            c += 0.5

    # Filter ans to show only sequences that are in ascending order and do not have starting zeros.

    ans = list(map(lambda x: x.split(','), ans))

    ans = list(filter(lambda x: not any(i for i in x if x[0] == '0'), ans))

    ans = list(map(lambda x: [int(i) for i in x], ans))

    ans = list(filter(lambda x: isInAscendingOrder(x), ans))

    return len(ans)

print(numberOfCombinations('9999999999'))

    


    







        






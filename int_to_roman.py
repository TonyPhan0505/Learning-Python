def intToRoman(num):
    num = int(num)
    roman = ''
    d = {1:'I', 5:'V', 10:'X', 50:'L', 90:'XC', 100:'C', 500:'D', 900:'CM', 1000:'M'}
    ans = []
    def find(num, roman):
        if num in list(d.keys()):
            roman += d[num]
            ans.append(roman)
        elif 1<num<1000:
            for i in range(len(list(d.keys()))):
                if list(d.keys())[i] - num > 1:
                    roman += d[list(d.keys())[i-1]]
                    find(num-list(d.keys())[i-1], roman)
                elif list(d.keys())[i] - num == 1:
                    roman += 'I' + d[list(d.keys())[i]]
                    ans.append(roman)

        elif num > 1000:
            roman += d[1000]
            find(num-1000, roman)

        return num, roman
    if num < 1:
        roman += 'Invalid'
    else:
        find(num, roman)
    return ans[0]
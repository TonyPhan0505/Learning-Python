from difflib import SequenceMatcher
import textwrap
from collections import Counter
from itertools import groupby
from itertools import product
import string
from collections import defaultdict
import random
import math   

def longestPalindrome(s):
    ans = []
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                ans.append(s[i:j+1])
    return max(ans, key = lambda x: len(x))

def anyWordWithDuplicateChars(s):
    for word in s.split():
        if len(word) > len(set(word)):
            return True
    return False

print(anyWordWithDuplicateChars("Filter out the factorials of the said list."))

def addStringsAsNums(n1, n2):
    if (n1.isnumeric() and n2.isnumeric()):
        return str(int(n1) + int(n2))
    else:
        return "Error"

def extract_digits(s):
    result = [int(n) for n in s.split() if n.isdigit()]
    return result

def similarity_check(str1,str2):
    result = SequenceMatcher(a = str1.lower(), b = str2.lower())
    return result.ratio()

def convert_lst_to_str(lst):
    return ','.join([str(x) for x in lst])

def remove_duplicate_words(str1):
    result = ''
    for word in str1.split():
        if word not in result: result += word
        else: pass
    return result

def remove_unwanted_chars(str1,unwanted_chars):
    for x in str1:
        if x in unwanted_chars: str1 = str1.replace(x,'')
    return str1

def check_string(str1):
    messg = []
    if not any (x.isupper() for x in str1): messg.append('String must have at least 1 uppercase')
    if not any (x.islower() for x in str1): messg.append('String must have at least 1 lowercase')
    if not any (x.isdigit() for x in str1): messg.append('String must have at least 1 nunber')
    if len(str1)<8: messg.append('String must be at least 8 characters long')
    if not messg: messg.append('Valid input')
    return messg

def find_common_value(str1,str2):
    result = ''.join(list(filter(lambda x: x in str2, str1)))
    return result

def remove_specific_char(str1,ch):
    result = ''.join(list(filter(lambda x: x != ch, str1)))
    return result

def swap_cases(s):
    result = ''.join(list(map(lambda x: x.lower() if x.isupper() else x.upper(), s)))
    return result

def wrap_text(s,width):
    return textwrap.fill(s,width)

def substringStartIndex(string,substring):
    l = len(substring)
    for i in range(len(string)):
        if string[i:i+l] == substring:
            return i
    return 'Not found'
    

def count_subs_with_sameEnds(str1):
    ctr = 0
    for i in range(len(str1)):
        for j in range(i,len(str1)):
            if str1[i] == str1[j]: ctr += 1
            else: pass
    return ctr

def find_longest_and_shortest_words(str1):
    words = str1.split()
    shortest = min(words, key = len)
    longest = max(words, key = len)
    return shortest, longest

def number_of_ch_in_alphabet_pos(str1):
    result = len(list(filter(lambda x: str1.index(x) == ord(x) - ord('a'), str1.lower())))
    return result

def number_of_possible_substrings(str1):
    return len(str1)*(len(str1)-1)/2

def count_upperLowerDigitSpecial(str1):
    upper_ctr, lower_ctr, numbers_ctr, special_ctr = 0,0,0,0
    for ch in str1:
        if ch.isupper(): upper_ctr += 1
        elif ch.islower(): lower_ctr += 1
        elif ch.isdigit(): numbers_ctr += 1
        else: special_ctr += 1
    return upper_ctr, lower_ctr, numbers_ctr, special_ctr

def filter_chars(str1,ch):
    result = ''.join(list(filter(lambda x: x == ch, str1)))
    return result

def move_spaces_to_front(str1):
    letters = [x for x in str1 if x != ' ']
    number_of_spaces = len(str1) - len(letters)
    spaces = ' '*number_of_spaces
    return spaces + ''.join(letters)

def concatenate_uncommon_chars(s1,s2):
    result = list(filter(lambda x: x not in s2, s1)) + list(filter(lambda x: x not in s1, s2))
    return ''.join(result)

def find_longest_common_string(str1,str2):
    match = SequenceMatcher(0,str1,str2)
    result = match.find_longest_match(0,len(str1),0,len(str2))
    if result.size != 0:
        return (str1[result.a:result.a+result.size])
    else: 
        return None

def generate_strings(str1):
    counts = Counter(str1)
    string1 = ''.join([key for (key,count) in counts.items() if count == 1])
    string2 = ''.join([key for (key,count) in counts.items() if count > 1])
    return string1, string2

def remove_consecutive_duplicate_chars(str1):
    result = [key for (key, group) in groupby(str1)]
    return ''.join(result)

def count_chars(s):
    counts = Counter(s)
    return counts

def count_removeables_in_anagram(str1,str2):
    result = len(list(filter(lambda x: x not in str2, str1)) + list(filter(lambda x: x not in str1, str2)))
    return result

def display_common_chars_in_lexi_order(str1,str2):
    common_chars = sorted(set(str1)&set(str2))
    if not common_chars: return 'No common characters'
    else: return common_chars

def maxLength_of_consecutiveZeros(str1):
    return max(map(len,str1.split('1')))

def remove_leading0s(str1):
    return '.'.join([str(int(x)) for x in str1.split('.')])

def sum_of_digits(str1):
    return sum([int(x) for x in str1 if x.isdigit()])

def remove_duplicate_chars(str1):
    result = ''
    for ch in str1:
        if ch not in result: result += ch
        else: pass
    return result

def capitalize_ends(str1):
    str1 = str1.title()
    result = ''
    for word in str1.split():
        result += word[:-1]+word[-1].upper()+' '
    return result[:-1]

def most_common_char(str1):
    temp = Counter(str1)
    keys = list(temp.keys())
    counts = list(temp.values())
    return keys[counts.index(max(counts))]

def second_most_repeated_word(str1):
    temp = {}
    for word in str1.split():
        if word not in temp: temp[word] = 1
        else: temp[word] += 1
    words_counts = list(temp.items())
    reversed_words_counts = sorted(words_counts,key = lambda x: x[1],reverse=True)
    return reversed_words_counts[1]

def first_repeated_word(str1):
    temp = []
    for word in str1.split():
        if word not in temp: temp.append(word)
        else: return word
    return None

def first_repeated_char(str1):
    result = ''
    for ch in str1:
        if ch not in result: result += ch
        else: return ch
    return None

def letterCombinations(digits):
    record = {
            '1': [''],
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r'],
            '8': ['s','t','u'],
            '9': ['v','w','x','y','z'],
    }
    answers = []
    for i in range(len(digits)):
        digit = digits[i]
        answer = record[digit]
        if not answers:
            answers = answer
        else:
            answers = [i + j for i in answers for j in answer]
    return answers

letterCombinations('23')

def arrangements(str1,rnum):
    return list(product(str1,repeat = int(rnum)))

def first_non_repeating_char(str1):
    for (index,ch) in enumerate(str1):
        if str1[:index+1].count(ch)>1: str1 = str1.replace(ch,'')
        else: pass
    return str1[0]

def split_string_on_last_occurrence(str1):
    return str1.rsplit(',',1)

def count_display_vowels(str1):
    vowels = ['a','o','e','u','i']
    temp = set()
    for ch in str1:
        if ch in vowels: temp.add(ch)
        else: pass
    return temp, len(temp)

def swap_comma_dot(str1):
    maketrans = str1.maketrans
    str1 = str1.translate(maketrans(',.','.,'))
    return str1

def lowercase_first_n_chars(str1,n):
    result = str1[:n].lower()+str1[n:]
    return result

def contain_all_alphabet(str1):
    alphabet = set(string.ascii_lowercase)
    return (set(str1.lower())>=alphabet)

def cm_squared():
    return 'cm\u00b2'

def count_repeatedChar(str1):
    counts = Counter(str1)
    temp = []
    for (key,count) in counts.items():
        if count > 1: temp.append((key,count))
        else: pass
    return temp

def reverse_wordsInString(str1):
    words = str1.split()
    return ' '.join(words[::-1])

def addTwoNumbers(l1, l2):
    sum = int(''.join([str(x) for x in l1[::-1]])) + int(''.join([str(x) for x in l2[::-1]]))
    print([int(n) for n in str(sum)][::-1])

def reverse_charsInString(str1):
    return ''.join(str1[::-1])

def count_occurrencesOfSubstring(str1,subs):
    return str1.count(subs)

def ten_points_left_align(str1,num):
    return '{:<10d}'.format(int(num))

def ten_points_right_align(str1,num):
    return '{:10d}'.format(int(num))

def ten_points_center_align(str1,num):
    return '{:^10d}'.format(int(num))

def percentage_form(num):
    return str((float(num)*100))+'%'

def comma_separated_number(num):
    return '{:,}'.format(int(num))

def caesar_encrypt(inText,step):
    outText = []
    uppercase_alphabet = list(string.ascii_uppercase)
    lowercase_alphabet = list(string.ascii_lowercase)

    for ch in inText:
        if ch in uppercase_alphabet:
            index = uppercase_alphabet.index()
            new_index = (index + step)%26
            new_ch = uppercase_alphabet[new_index]
            outText.append(new_ch)
        elif ch in lowercase_alphabet:
            index = uppercase_alphabet.index()
            new_index = (index + step)%26
            new_ch = uppercase_alphabet[new_index]
            outText.append(new_ch)
        else: outText.append(ch)
    
    return ''.join(outText)


def findMedianSortedArrays(nums1, nums2):
    all = sorted(nums1 + nums2)
    if len(all) %2 == 0:
        return (all[int(len(all)/2 - 1)] + all[int(len(all)/2)])/2
    else:
        return all[int(len(all)/2 - 0.5)]

print(findMedianSortedArrays([1,3], [2]))

def add_prefix(str1):
    return textwrap.indent(text = str1, prefix = 'Name:')

def count_substring_k_dist(str1,k):
    ctr = 0
    for i in range(len(str1)-k+1):
        if len(set(str1[i:i+k])) == k: ctr += 1
    return ctr
   
def get_anagrams(words_lst):
    d = defaultdict(list)
    for word in words_lst:
        key = "".join(sorted(word))
        d[key].append(word)
    return d

def print_anagrams(words_lst):
    anagrams = get_anagrams(words_lst)
    result = [i[1] for i in anagrams.items() if len(i[1]) > 1]
    return result

def minimum_window(s, t):

	answer = ''

	if len(s) == len(t):

		answer = s

	else:

		req = Counter(t)

		l, r = 0, 0

		while r < len(s):

			while l < r:

				min_window = s[l:r+1]

				min_window_counts = Counter(min_window)

				if len([c for c in min_window if c in t]) == len(t):

					answer = min_window

				l += 1

			l = 0

			r += 1

		l, r = 0, len(answer)-1

		while l < r:

			r -= 1

			if len([c for c in answer[l:r+1] if c in t]) == len(t):

				answer = answer[l:r+1]

	return answer

def most_diverse_substring(str1):
    curr_count = Counter(str1)
    reqs = list(curr_count.keys())
    sorted_reqs = "".join(sorted(reqs))
    for i in range(len(str1)):
        for j in range(i, len(str1)):
            end_index = i+j+1
            substring = str1[i:end_index]
            if "".join(sorted(substring)) == sorted_reqs:
                return substring
            else: pass
    return None

def random_password(length):

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = '0123456789'
    symbols = '~`!@#$%^&*()_-+=[]}{\|'

    all = lower + upper + numbers + symbols
    password = ''.join(random.sample(all, length))
    return password

def pairing(l1, l2):
	ans = []
	for i in range(len(l1)):
		for j in range(len(l2)):
			ans.extend([l1[i],l2[j]])
	return ans

def is_array_empty(array):
    return True if not len(array) else False

# 1. Put '(' = '1' and ')' = 0.
# 2. Create a list to put answers in.
# 3. Set a base answer. Other answers are well-formed transformations of the base answer. Base answer = '1'*n + '0'*n.
# 4. Move the last '1' to the right one step at a time until it reaches pos = -2
# 5. Continue step 3 with the remaining '1's until there each '1' has a '0' on its right.
# 6. Move the last '1' to the left one step at a time until it reaches pos = 1.
# 7. Filter out all repeated answers in the list.
# 8. Translate 1s and 0s in the list into '('s and ')'s.
# 9. Return the list.

def generateParenthesis(n):
    
    if n == 1:
        return ['()']

    base = '('*n + ')'*n

    ans = [base]

    j = n - 1
    
    chars = [x for x in base]

    while j > 0:
        
        i = t = j
        
        while i < t*2:

            chars[i], chars[i+1] = chars[i+1], chars[i]

            a = ''.join(chars)

            ans.append(a)
            
            i += 1

        j -= 1

    k = -2

    while k > -(len(base)-1):
        
        if chars[k] != chars[k-1]:

            chars[k], chars[k-1] = chars[k-1], chars[k]

            a = ''.join(chars)

            if a not in ans:

                ans.append(a)

        k -= 1

    return ans

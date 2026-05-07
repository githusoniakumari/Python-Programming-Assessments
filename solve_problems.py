'''
# 1. Extract all string data items from a list
c= [10, 'Hello', 20.5, 'world', [1, 2], 'python']
for i in c:
    if i == str(i):
        print(i)

# 2. Count uppercase letters using recursion
def count_upper(s, i=0):
    if i == len(s):
        return 0
    if 'A' <= s[i] <= 'Z':
        return 1 + count_upper(s, i + 1)
    return count_upper(s, i + 1)

print(count_upper("ReCurSion In PyThOn"))


# 3. Print list data items in tuple only if they have a middle value
t = (10, [1, 2, 3], "hello", [9, 0], [4])

for i in t:
    if isinstance(i, list):
        if len(i) % 2 == 1:
            print(i)


# 4. Reverse an integer without slicing or typecasting
def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev

print(reverse_number(12345))


# 5. Check if a number is a strong number
def factorial(n):
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f

def is_strong(n):
    sum_fact = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum_fact += factorial(digit)
        temp = temp // 10
    return sum_fact == n

print(is_strong(145))


'''
# 6. Get specific format using recursion
def custom_case(s, i=0, out=[], w="", pos=0):
    if i == len(s):
        out.append(w)
        return out
    if s[i] == ' ':
        out.append(w)
        return custom_case(s, i+1, out, "", 0)
    if pos % 2 == 0 and 'a' <= s[i] <= 'z':
        w += chr(ord(s[i]) - 32)
    elif pos % 2 == 1 and 'A' <= s[i] <= 'Z':
        w += chr(ord(s[i]) + 32)
    else:
        w += s[i]
    return custom_case(s, i+1, out, w, pos+1)

print(custom_case("recursion is easy"))

'''
# 7. Count words with specific rule
s = 'Sun moon Star'
words = []
temp = ""
for ch in s:
    if ch == ' ':
        words.append(temp)
        temp = ""
    else:
        temp += ch
words.append(temp)

output = {}
for word in words:
    if word == 'moon':
        output[word] = 2
    else:
        output[word] = 1
print(output)
'''

'''
# 8. Extract special characters
s = "Hello! This# is$ a@ test% string^"
specials = ""
for ch in s:
    if not ('A' <= ch <= 'Z' or 'a' <= ch <= 'z' or '0' <= ch <= '9' or ch == ' '):
        specials += ch
print(specials)
'''
'''
# 9. Create list of uppercase A–Z
uppercase = []
for i in range(65, 91):
    uppercase.append(chr(i))
print(uppercase)
'''
'''
# 10. Reverse dictionary from sentence
s = 'hai hello how are you'
words = []
temp = ''
for ch in s:
    if ch == ' ':
        words.append(temp)
        temp = ''
    else:
        temp += ch
words.append(temp)

output = {}
for i in range(len(words)):
    output[words[i]] = words[len(words) - 1 - i]
print(output)
'''

'''
# 11. Map lowercase to position
s = "'A''b''C''d''E''z'"
i = 0
output = []
while i < len(s):
    if s[i] == "'":
        char = s[i+1]
        if 'a' <= char <= 'z':
            output.append(ord(char) - 96)
        else:
            output.append(char)
        i += 3
    else:
        i += 1
print(output)
'''
'''
# 12. Odd index string check
lst = [1, 'a', 3, 'b', 5, 'c']
if len(lst) % 2 == 0:
    print("hello")
else:
    out = []
    concat = ''
    valid = True
    for i in range(len(lst)):
        if i % 2 == 1:
            if lst[i] == str(lst[i]):
                concat += lst[i]
            else:
                valid = False
                break
    if valid and concat != '':
        print(concat)
    else:
        print(lst)
'''

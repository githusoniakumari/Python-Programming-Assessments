"""
#1
def extract_strings(lst, index=0, result=None):
    if result is None:
        result = []
    if index == len(lst):
        return result
    if type(lst[index]) == str:
        result.append(lst[index])
    return extract_strings(lst, index + 1, result)

lst = [1, 'apple', 2, 'banana', 3.5, 'cherry']
print(extract_strings(lst))

#2

def count_uppercase(s, index=0, count=0):
    if index == len(s):
        return count
    if s[index].isupper():
        count += 1
    return count_uppercase(s, index + 1, count)


input_string = "Hello World!"
print(count_uppercase(input_string))

#3
def print_middle_value_lists(tpl, index=0):
    if index == len(tpl):
        return
    if type(tpl[index]) == tuple:  
        if len(tpl[index]) % 2 != 0:  
            print(tpl[index])
    return print_middle_value_lists(tpl, index + 1)


tpl = (1, (2, 3, 4), 'Hello', (5, 6, 7, 8, 9))
print_middle_value_lists(tpl)

#4
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    rev = rev * 10 + n % 10
    return reverse_number(n // 10, rev)

input_number = 12345
print(reverse_number(input_number))


#5

def fact(num):
    if num == 0 or num == 1:
        return 1
    return num * fact(num - 1)

def is_strong_number(n, temp=None, sum_fact=0):
    if temp is None:
        temp = n
    if temp == 0:
        return sum_fact == n
    last_digit = temp % 10
    sum_fact += fact(last_digit)
    return is_strong_number(n, temp // 10, sum_fact)

number = int(input("enter the number: "))
print(is_strong_number(number)) 



#6
def fname(input_str):
    result = []
    i = 0
    while i < len(input_str):
        current = ""
        while i < len(input_str) and input_str[i] != ' ':
            if i % 2 == 0:
                current += input_str[i].upper()
            else:
                current += input_str[i].lower()
            i += 1
        result.append(current)
        i += 1
    return " ".join(result)

#input_string = 'recursion is easy'
input_string = input(" enter the string: ")
print(fname(input_string))

#7
def word_count(input_str, index=0, word_dict=None):
    if word_dict is None:
        word_dict = {}
    if index == len(input_str.split()):
        return word_dict
    
    word = input_str.split()[index]
    word_dict[word] = word_dict.get(word, 0) + 1
    return word_count(input_str, index + 1, word_dict)

input_string = input("enter the string: ")
print(word_count(input_string))
"""

# 8
def extract_special_characters(s, index=0, result=None):
    if result is None:
        result = []
    if index == len(s):
        return result
    if not s[index].isalnum() and s[index] != ' ':
        result.append(s[index])
    return extract_special_characters(s, index + 1, result)

input_string = input("enter the string: ") 
print(extract_special_characters(input_string))
















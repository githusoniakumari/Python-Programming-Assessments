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


# 9
def uppercase_alphabets(index=0, result=None):
    if result is None:
        result = []
    if index == 26:
        return result
    result.append(chr(ord('A') + index))
    return uppercase_alphabets(index + 1, result)

print(uppercase_alphabets())

# 10
def reverse_pairs(words, index=0, result=None):
    if result is None:
        result = {}
    if index == len(words):
        return result
    result[words[index]] = words[len(words) - 1 - index]
    return reverse_pairs(words, index + 1, result)

input_string = input("enter a string: ") 
print(reverse_pairs(input_string.split()))

#11
def process_characters(chars, index=0, result=None):
    if result is None:
        result = []
    if index == len(chars):
        return result
    if chars[index].islower():
        result.append(ord(chars[index]) - ord('a') + 1)
    else:
        result.append(chars[index])
    return process_characters(chars, index + 1, result)

input_chars = "aBzXc"
print(process_characters(input_chars))


# 12
def process_odd_indices(lst, index=1, result=None):
    if result is None:
        result = []
    if index >= len(lst):
        if len(lst) % 2 == 0:
            print("hello")
        else:
            print(result)
        return
    if type(lst[index]) == str:
        result.append(lst[index])
    process_odd_indices(lst, index + 2, result)

lst = [1, "apple", 3, "banana", 5]
process_odd_indices(lst)
"""

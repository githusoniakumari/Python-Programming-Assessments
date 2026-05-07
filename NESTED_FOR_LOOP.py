S = 'kabab is love'
vowels = "aeiou"
result = {}
word = " "
reverse_word = " "
count_vowels = 0
even_index_chars = " "

for i in range(len(S) + 1):
    if i < len(S) and S[i] != " ":
        word += S[i]
        reverse_word = S[i] + reverse_word  
        if i % 2 == 0:
            even_index_chars += S[i]
        for v in vowels:
            if S[i] == v:
                count_vowels += 1
    else:
        if word:
            key = " "
            for char in word:
                key += char
            result[key] = [reverse_word, count_vowels, even_index_chars]
        word = " "
        reverse_word = " "
        count_vowels = 0
        even_index_chars = ""

print(result)

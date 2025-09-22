# s = "PythonLearning"

# print(s[0])      # First char → P
# print(s[-1])     # Last char → g
# print(s[0:6])    # Slice first 6 chars → Python
# print(s[6:])     # From 6th char onwards → Learning
# print(s[:6])     # Up to 6th char → Python
# print(s[::2])    # Every 2nd char → PtoLann
# print(s[::-1])   # Reverse the string → gninraeLnothyP



# word = "ArtificialIntelligence"

# print(word[:10])
# print(word[10:])
# print(word[::-1])

# sentence = "Deep Learning with Python is powerful"

# # print(sentence.upper())
# # if sentence.startswith('Deep'):
# #     print('True')
# # else:
# #     print('False')

# # print(sentence.replace('powerful','amazing'))
# # print(sentence.find('Python'))

# for index,char in enumerate(sentence):
#     print(index,char)


quote = "Data Science with Python and AI"


for index,char in enumerate(quote):
    print(index,char)

print(quote[0:4])
print(quote[5:12])
print(quote[18:24])
print(quote.replace('AI','Machine Learning'))
print(quote.lower())
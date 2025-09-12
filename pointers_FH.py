# with open("sample.txt",'w') as f:
#     f.write('Python is amazing!\n')
#     f.write('File handling is powerful.\n')


# with open('sample.txt','r') as f:
#     first_part=f.read(10)
#     print(f'Read first 10 characters - {first_part}')

#     print(f'Pointer location - {f.tell()}')

#     f.seek(0)

#     full_content=f.read()

#     print(f'Full content - {full_content}')

# ---------------------------------------------------------------------------------------------------------------------
# Word & Line Counter

# def file_stats(filename):
#     with open(filename,'r') as f:
#         lines=f.readlines()

#         num_lines=len(lines)
#         num_words=sum(len(line.split()) for line in lines)
#         num_chars=sum(len(line) for line in lines)

#         return num_lines,num_words,num_chars
    
# lines,words,chars = file_stats('sample.txt')

# print(f'No of lines - {lines}')
# print(f'No of words - {words}')
# print(f'No of chars - {chars}')

# ------------------------------------------------------------------------------------------------------------------
# word frequency

# from collections import Counter
# import re

# def word_frequency(filename):
#     with open(filename,'r') as f:
#         text=f.read().lower()

#         # regex
#         words=re.findall(r"\b[a-zA-Z]+\b",text)

#         freq=Counter(words)

#         return(freq)
    
# # Usage
# freq = word_frequency("sample.txt")

# # Print top 5 most common words
# for word, count in freq.most_common(5):
#     print(word, ":", count)

# -----------------------------------------------------------------------------------------------------------------------

# Word Frequency Bar Chart

from collections import Counter
import re
import matplotlib.pyplot as plt

def word_frequency(filename,top_n=10):
    with open('sample.txt','r') as f:
        text=f.read().lower()

        words=re.findall(r"\b[a-zA-z]+\b",text)

        freq=Counter(words)

        return freq.most_common(top_n)
    
# Usage
top_words = word_frequency("sample.txt", top_n=5)

# Separate words and counts for plotting
words, counts = zip(*top_words)

# Plot
plt.bar(words, counts)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top Word Frequencies")

plt.savefig('Words frequency plot.png',dpi=300,bbox_inches='tight')

plt.show()
    


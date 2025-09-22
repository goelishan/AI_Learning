from collections import Counter
import re
import matplotlib.pyplot as plt

def file_stats(filename):
    with open(filename,'r')as f:
        lines=f.readlines()

    num_lines=len(lines)
    num_words=sum(len(line.split()) for line in lines)
    num_chars=sum(len(lines) for line in lines)

    return num_lines,num_words,num_chars


def word_frequency(filename,top_n=10):
    with open(filename,'r') as f:
        text=f.read().lower()

    words=re.findall(r"\b[a-zA-Z]+\b",text)
    freq=Counter(words)
    return freq.most_common(top_n)

def file_analyze(filename,top_n=10):

    lines,words,chars=file_stats(filename)

    print(f'File - {filename}')
    print(f'Lines - {lines}, Words - {words}, Chars - {chars}')

    top_words=word_frequency(filename,top_n)
    print('\n Top Words')

    for word,count in top_words:
        print(f'{word} - {count}')

    if top_words:
        words,counts=zip(*top_words)
        plt.bar(words,counts, color='skyblue')
        plt.xlabel('Words')
        plt.ylabel('Frequency')
        plt.title(f'Top {top_n} Word Frequencies')
        plt.show()
        


file_analyze('sample.txt',top_n=5)





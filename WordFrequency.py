file_name = 'sometext.txt'

word_freq = {}
punctuation = [',','.','!','?','(',')','"','/',':',';','-']
clean_words=[]

file = open(file_name,'r')
fileread = file.read()
words = fileread.split()

for word in words:
    for p in punctuation:
        word = word.replace(p,'').lower()
    clean_words.append(word)

for word in clean_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

file.close()

print(word_freq)
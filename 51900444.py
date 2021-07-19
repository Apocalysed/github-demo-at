import nltk
s = []
s.append('cô ấy dạy môn tin học')
s.append('anh dạy môn toán')
s.append('cô ấy học toán anh ấy dạy')
s.append('môn toán môn tin đều hay')
s.append('anh ấy dạy môn toán hay môn tin')
words = nltk.word_tokenize(s[0])
print(words)
'''unigram_dict={}
total_count = 0
for sent in s:
    word = nltk.word_tokenize(sent)
    total_count += len(words)
    for w in words:
        if w in unigram_dict.keys{};
            unigram_dict[w] += 1
        else:
            unigram_dict[w] += 1
print(unigram_dict)
print(total_count)
input_sent = 'anh dạy môn tin học'
words = nltk.word_tokenize(input_sent)
p = 1
for w in words:
    if w in unigram_dict.keys{};
        p *= unigram_dict[w]/total_count
    else:
        p = 0
        break
print(p)'''
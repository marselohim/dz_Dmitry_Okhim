sentence = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'граддусов']
sentence.insert(1, '"')
sentence.insert(3, '"')
sentence.insert(5, '"')
sentence.insert(7, '"')
sentence.insert(12, '"')
sentence.insert(14, '"')
for item in sentence:
    sentence[2] = sentence[2].zfill(2)
    sentence[13] = sentence[13][sentence[13].index('+'):].zfill(3)
' '.join(sentence)
print(' '.join(sentence))

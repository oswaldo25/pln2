
import nltk

sentence =  "C:\Users\Sherl\Documents\PNL"
tokens = nltk.word_tokenize(sentence)


tagged = nltk.pos_tag(tokens)
tagged[0:6]


from nltk.corpus import treebank
t = treebank.parsed_sents('texto.txt')[0]
t.draw()
import nltk
from nltk import word_tokenize
from nltk.util import ngrams

sentence = "I am learning AI with Codedex"
tokens = word_tokenize(sentence)
unigrams = list(ngrams(tokens,1))
print("Uni: ",unigrams)
bigrams = list(ngrams(tokens,2))
print("Bi: ", bigrams)
trigrams = list(ngrams(tokens,3))
print("Tri: ", trigrams)
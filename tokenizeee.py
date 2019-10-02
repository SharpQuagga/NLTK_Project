from nltk.tokenize import sent_tokenize, word_tokenize

e_text = "Hello Mr. Smith, how are you doing today? The weather is geart and python is awesome."

print(sent_tokenize(e_text))
print(word_tokenize(e_text))
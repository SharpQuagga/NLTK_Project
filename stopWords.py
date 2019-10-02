from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

e_sent = "This is an to example show off stop-word filtration"
stop_words = set(stopwords.words("english"))
words = word_tokenize(e_sent)

filtered_sent = [w for w in words if not w in stop_words]

print(filtered_sent)
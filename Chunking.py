import nltk
from nltk.corpus import state_union
from nltk.tokenize import sent_tokenize
# from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

# custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
# tokenized = custom_sent_tokenizer(sample_text)
tokenized = sent_tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()
    except Exception as e:
        print(str(e))

process_content()

# Another term is chinking , it's exactly opposite of this 
#  We just remove the terms we don't want instead of taking the terms we want


"""
This line, broken down:
<RB.?>* = "0 or more of any tense of adverb," followed by:
<VB.?>* = "0 or more of any tense of verb," followed by:
<NNP>+ = "One or more proper nouns," followed by
<NN>? = "zero or one singular noun."

"""
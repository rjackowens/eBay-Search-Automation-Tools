import spacy
# from spacy.lang.en.stop_words import STOP_WORDS # Imports Default List of Stop Words
# STOP_WORDS.add("ORION") # This adds  

# Imports List of Custom Stop Words
with open("watchfilter.txt", "r") as filter:
    custom_stop_words = filter.read().splitlines()

# Init spaCy Language Model + Example Title
nlp = spacy.load('en_core_web_sm')
doc = nlp(u"Good Condition Jaeger LeCoultre Master Ultra Thin 145.2.79.S Diamond 18K Rose Gold") # Doc Type is <class 'spacy.tokens.doc.Doc'>

# Add Custom Stop Words to spaCy
for stopword in custom_stop_words:
    lexeme = nlp.vocab[stopword]
    lexeme.is_stop = True

# Removes Keywords Included on Stop Word List
words_filtered =[]
for token in doc:
    #print(token.is_stop) 
    if token.is_stop != True:
        words_filtered.append(token)

print(*words_filtered, sep=" ")

import random
from PyDictionary import PyDictionary
dictionary=PyDictionary()
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


currentMessage = input("Input a sentence:\n")

is_noun = lambda pos: pos[:2] == 'NN'
is_verb = lambda pos: pos[:2] == 'VB'
is_adj = lambda pos: pos[:2] == 'JJ'
tokenized = nltk.word_tokenize(currentMessage)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
verbs = [word for (word, pos) in nltk.pos_tag(tokenized) if is_verb(pos)] 
adjectives = [word for (word, pos) in nltk.pos_tag(tokenized) if is_adj(pos)]
nounLen = len(nouns)
verbLen = len(verbs)
adjLen = len(adjectives)

print("nouns:", nounLen, "\nverbs:", verbLen, "\nadjectives:", adjLen)
print(sia.polarity_scores(currentMessage))

# sentenceLength = len(currentMessage.split())
# choosingNum = random.randint(0,sentenceLength-1)
# sentenceSplit = (currentMessage.split())
# chosenWord = sentenceSplit[choosingNum]
# # print(chosenWord)
# thesaurus =  (dictionary.synonym(chosenWord))
# # print(thesaurus)
# if (thesaurus != None):
#     thesLength = len(thesaurus)
#     choosingThesNum = random.randint(0,thesLength-1)
#     chosenThesWord = thesaurus[choosingThesNum]

#     sentenceSplit.remove(chosenWord)
#     sentenceSplit.insert(choosingNum,chosenThesWord)
#     sentenceReword = ' '.join(sentenceSplit)
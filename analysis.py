import nltk
import os
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer

x=TweetTokenizer()
stopwords= set(stopwords.words('english'))

# returns a dictionary with word and integer frequency
def generateFrequencyMap(words):
    pass
with open('Godfather1.txt') as godfatha:
    lines =[line.strip() for line in godfatha.readlines()]
    lines =' '.join(lines)

godfather1Tokens= [word.lower() for word in x.tokenize(lines) if word.lower() not in stopwords and len(word)>1 and word!='...' and word!='... ...' and word!='. ...']

with open('Godfather2.txt') as godfatha:
    lines =[line.strip() for line in godfatha.readlines()]
    lines =' '.join(lines)
# had to account for some random dots
godfather2Tokens= [word.lower() for word in x.tokenize(lines) if word.lower() not in stopwords and len(word)>1 and word!='...' and word!='... ...' and word!='. ...']

with open('Godfather2Words.txt','w') as godfatha:
    for line in godfather2Tokens:
        godfatha.write(line+"\n")
        
with open('Godfather1Words.txt','w') as godfatha:
    for line in godfather1Tokens:
        godfatha.write(line+"\n")
# Using cli to generate plots
os.system('wordcloud_cli --text Godfather1Words.txt --imagefile Godfather1.png --width 1000 --height 1000 ')
os.system('wordcloud_cli --text Godfather2Words.txt --imagefile Godfather2.png --width 1000 --height 1000')

print(godfather1Tokens)
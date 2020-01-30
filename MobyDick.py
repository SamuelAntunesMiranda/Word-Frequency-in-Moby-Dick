from bs4 import BeautifulSoup
import requests
import nltk

#web scrapping for the Moby Dick book
r = requests.get('https://s3.amazonaws.com/assets.datacamp.com/production/project_147/datasets/2701-h.htm')
r.encoding = 'utf-8'
html = r.text
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()
#creating an array that only has the words, removing spaces, commas etc.
tokenizer = nltk.tokenize.RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(text)
words = []
#making every word lowercase
for word in tokens:
    words.append(word.lower())
#getting the stop words for the english language
sw = nltk.corpus.stopwords.words('english')
words_ns = []
#creating an array without the stop words
for word in words:
    if word not in sw:
        words_ns.append(word)

#using nltk frequency distribution function to get the most commom word in the array
#without the stop words.
freqdist = nltk.FreqDist(words_ns)
print(freqdist.most_common(1))

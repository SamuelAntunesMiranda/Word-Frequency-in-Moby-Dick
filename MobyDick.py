from bs4 import BeautifulSoup
import requests
import nltk

r = requests.get('https://s3.amazonaws.com/assets.datacamp.com/production/project_147/datasets/2701-h.htm')
r.encoding = 'utf-8'
html = r.text
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()
tokenizer = nltk.tokenize.RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(text)
words = []

for word in tokens:
    words.append(word.lower())

sw = nltk.corpus.stopwords.words('english')
words_ns = []
for word in words:
    if word not in sw:
        words_ns.append(word)


freqdist = nltk.FreqDist(words_ns)
print(freqdist.most_common(1))

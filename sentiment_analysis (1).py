# -*- coding: utf-8 -*-
"""Sentiment_Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1b8jeNtzpzkHP0VwwwZlld4n_A1Pvpf0x
"""

from google.colab import files


uploaded = files.upload()

import pandas as pd
import io
data = pd.read_csv(io.BytesIO(uploaded['Reviews.csv']))
print(data)



data

# checking the null values
data.isnull().sum()

#checking the duplicate data
data.duplicated()

#exploratary data analysis matplotlib and seborn
import seaborn as sns
import matplotlib.pyplot as plt

from wordcloud import WordCloud

combined_text = " ".join(data['Review']) #combine all review text into one string
combined_text

wordcloud = WordCloud(width=800, height = 400, background_color = 'white').generate(combined_text)

plt.figure(figsize=(15,6))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.title('word cloud of Reviews')
plt.show()

from collections import Counter

targeted_words = ['good','great','amazing','bad','nor bad']
all_words=" ".join(data['Review']).lower().split() #flatten reviews into a single list of words
word_counts = Counter(all_words)
target_word_count={word: word_counts[word] for word in targeted_words}

plt.figure(figsize=(8,6))
plt.bar(target_word_count.keys(), target_word_count.values(), color=['blue','green','orange','red','black'])
plt.xlabel('words')
plt.ylabel('frequency')
plt.title('Frequency of specific words in reviews')
plt.show()

#Text PreProcessing

#converting a datset into a lowercase
lowercased_text=data['Review'].str.lower()
print(lowercased_text)

import nltk
nltk.download('punkt')
nltk.download('stopwords')

#tokenization (its a NLP model)
#(converts the sequence of text words into smaller parts known as tokens)
from nltk.tokenize import word_tokenize

data['Tokens']=data['Review'].apply(word_tokenize)
print(data['Tokens'])

data.info()

#REmoving stop words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words=set(stopwords.words('english'))

data['Tokens']=data['Tokens'].apply(lambda x: [word for word in x if word not in stop_words])

print(data['Tokens'])

data.info()

#Stemming (Stemming is a text preprocessing technique in natural language processing (NLP)
#it is a processing of reducing the inflected word to root form )

from nltk.stem import PorterStemmer
#from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

data['stemmed']=data['Review'].apply(lambda x: [stemmer.stem(word) for word in word_tokenize(x)])

print(data['stemmed'])

#Lemmatization

import nltk
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

lemmatizer = WordNetLemmatizer()

data['Lemmatized'] = data['Review'].apply(lambda x:' '.join([lemmatizer.lemmatize(word,pos=wordnet.VERB) for word in word_tokenize(x)]))

print(data['Lemmatized'])

#rRemove the numbers

import re
data['No_Numbers']=data['Review'].apply(lambda x: re.sub(r'\d+','',x))

print(data['No_Numbers'])

data['cleaned_text']=data['Review'].apply(lambda x: re.sub(r'[^A-Za-z0-9\s]',' ',x))

print(data['cleaned_text'])

data.info()

#Normaliztion
#!pip install contractions
import contractions
data['Expandes']=data['Review'].apply(lambda x: contractions.fix)
print(data['Expandes'])

#Removing the emojis
#!pip install emoji

import emoji
data['Emoji']=data['Review'].apply(emoji.demojize)
print(data['Emoji'])

!pip install beautifulsoup4

#for removing the html tags we need to install the beautifulsoup4 library
from bs4 import BeautifulSoup
data['cleaned']=data['Review'].apply(lambda x: BeautifulSoup(x,"html.parser").get_text())

print(data['cleaned'])


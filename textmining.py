# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 12:54:52 2021

@author: prash
"""
#1.	Extract reviews of any product from e-commerce website Amazon.
import requests   # Importing requests to extract content from a url
from bs4 import BeautifulSoup as bs # Beautifulsoup is for web scrapping...used to scrap specific content 
import re 

import matplotlib.pyplot as plt
from wordcloud import WordCloud


# creating empty reviews list 
Googlepixel_reviews=[]


for i in range(1,20):
  ip=[]  
  url="https://www.amazon.in/Google-Pixel-Black-128GB-Storage/product-reviews/B08CFSZLQ4/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews="+str(i)
  response = requests.get(url)
  soup = bs(response.content,"html.parser")# creating soup object to iterate over the extracted content 
  reviews = soup.find_all("div",attrs={"class","a-row a-spacing-small review-data"})# Extracting the content under specific tags  
  for i in range(len(reviews)):
    ip.append(reviews[i].text) 
  Googlepixel_reviews=Googlepixel_reviews+ip  #adding the reviews of one page to empty list which in future contains all the reviews


 # writng reviews in a text file 
with open("Googlepixel.txt","w",encoding='utf8') as output:
    output.write(str(Googlepixel_reviews))
	
# Joinining all the reviews into single paragraph 
ip_rev_string = " ".join(Googlepixel_reviews)

import nltk
# from nltk.corpus import stopwords


# Removing unwanted symbols incase if exists
ip_rev_string = re.sub("[^A-Za-z" "]+"," ", ip_rev_string).lower()
ip_rev_string = re.sub("[0-9" "]+"," ", ip_rev_string)

# words that contained in iphone XR reviews
ip_reviews_words = ip_rev_string.split(" ")

#TFIDF
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(ip_reviews_words, use_idf=True,ngram_range=(1, 3))
X = vectorizer.fit_transform(ip_reviews_words)

with open("C:\\Users\\prash\\Desktop\\ASIGNMENT\\TEXT MINING\\stopwords.txt","r") as sw:
    stopwords = sw.read()
    
stopwords=stopwords.split("\n")
stopwords.extend(["google","pixel","mobile","time","android","phone","device","screen","battery","product","good","day","price"])

ip_reviews_words = [w for w in ip_reviews_words if not w in stopwords]


# Joinining all the reviews into single paragraph 
ip_rev_string = " ".join(ip_reviews_words)


#WORDCLOUD:-
# WordCloud can be performed on the string inputs.
# Corpus level word cloud

wordcloud_ip = WordCloud(
                      background_color='White',  repeat=False,
                      width=2000,
                      height=1500
                     ).generate(ip_rev_string)

plt.imshow(wordcloud_ip)


#########################################################################

#2.Perform sentiment analysis on this extracted data and build a unigram and bigram word cloud

import nltk
nltk.download('punkt')

word_data =" browser support html video light excellent design camera superb overall experience flawless competetive imported brilliant size little xl range phones speaker mind boggling camera world buy doubts recieved warranty card rd using amazing camera quality easy worth money coz reasons form factor age epidemic inch slabs messiah example phones imo inches perfect size smartphone keeping ur pocket operating hand camera guesses photo processing smartphones clicks pics little noise especially love night mode fan mode reasons switch previous yr yeah lasts dont worry carrying power banks play heavy games run faster delivery timeproduct quality received display issue word return replacement update jan month support based experience request buy seller rip money purchased value money look retail options amazon fullfillment policy vendor strikehrough comment added amzn feedback https www amazon gp help seller glance html ref ppx od dt sellerprofile ie utf isamazonfulfilled marketplaceseller orderid seller ev fczwl exited piece month usage found backup bad charge drain bedtime internet watching videos difficulties module nice compact night mode nice potrait mode takes process result fantastic days usage found heavy gamer camera calls smooth hz bit slippery hand protect hand fingerprint unlock unlock fast iphone otherwise speed camera equals iphone edited week usage found optimized getting solid nice light weight size comfortable handle ideal searching excellent hope won regret browser support html video light excellent design camera superb overall experience flawless competetive imported brilliant size little xl range phones speaker mind boggling camera world buy doubts recieved warranty card rd using amazing camera quality easy worth money coz reasons form factor age epidemic inch slabs messiah example phones imo inches perfect size smartphone keeping ur pocket operating hand camera guesses photo processing smartphones clicks pics little noise especially love night mode fan mode reasons switch previous yr yeah lasts dont worry carrying power banks play heavy games run faster delivery timeproduct quality received display issue word return replacement update jan month support based experience request buy seller rip money purchased value money look retail options amazon fullfillment policy vendor strikehrough comment added amzn feedback https www amazon gp help seller glance html ref ppx od dt sellerprofile ie utf isamazonfulfilled marketplaceseller orderid seller ev fczwl exited piece month usage found backup bad charge drain bedtime internet watching videos difficulties module nice compact night mode nice potrait mode takes process result fantastic days usage found heavy gamer camera calls smooth hz bit slippery hand protect hand fingerprint unlock unlock fast iphone otherwise speed camera equals iphone edited week usage found optimized getting solid nice light weight size comfortable handle ideal searching excellent hope won regret browser support html video light excellent design camera superb overall experience flawless competetive imported brilliant size little xl range phones speaker mind boggling camera world buy doubts recieved warranty card rd using amazing camera quality easy worth money coz reasons form factor age epidemic inch slabs messiah example phones imo inches perfect size smartphone keeping ur pocket operating hand camera guesses photo processing smartphones clicks pics little noise especially love night mode fan mode reasons switch previous yr yeah lasts dont worry carrying power banks play heavy games run faster delivery timeproduct quality received display issue word return replacement update jan month support based experience request buy seller rip money purchased value money look retail options amazon fullfillment policy vendor strikehrough comment added amzn feedback https www amazon gp help seller glance html ref ppx od dt sellerprofile ie utf isamazonfulfilled marketplaceseller orderid seller ev fczwl exited piece month usage found backup bad charge drain bedtime internet watching videos difficulties module nice compact night mode nice potrait mode takes process result fantastic days usage found heavy gamer camera calls smooth hz bit slippery hand protect hand fingerprint unlock unlock fast iphone otherwise speed camera equals iphone edited week usage found optimized getting solid nice light weight size comfortable handle ideal searching excellent hope won regret browser support html video light excellent design camera superb overall experience flawless competetive imported brilliant size little xl range phones speaker mind boggling camera world buy doubts recieved warranty card rd using amazing camera quality easy worth money coz reasons form factor age epidemic inch slabs messiah example phones imo inches perfect size smartphone keeping ur pocket operating hand camera guesses photo processing smartphones clicks pics little noise especially love night mode fan mode reasons switch previous yr yeah lasts dont worry carrying power banks play heavy games run faster delivery timeproduct quality received display issue word return replacement update jan month support based experience request buy seller rip money purchased value money look retail options amazon fullfillment policy vendor strikehrough comment added amzn feedback https www amazon gp help seller glance html ref ppx od dt sellerprofile ie utf isamazonfulfilled marketplaceseller orderid seller ev fczwl exited piece month usage found backup bad charge drain bedtime internet watching videos difficulties module nice compact night mode nice potrait mode takes process result fantastic days usage found heavy gamer camera calls smooth hz bit slippery hand protect hand fingerprint unlock unlock fast iphone otherwise speed camera equals iphone edited week usage found optimized getting solid nice light weight size comfortable handle ideal searching excellent hope won regret browser support html video light excellent design camera superb overall experience flawless competetive imported brilliant size little xl range phones speaker mind boggling camera world buy doubts recieved warranty card rd using amazing camera quality easy worth money coz reasons form factor age epidemic inch slabs messiah example phones imo inches perfect size smartphone keeping ur pocket operating hand camera guesses photo processing smartphones clicks pics little noise especially love night mode fan mode reasons switch previous yr yeah lasts dont worry carrying power banks play heavy games run faster delivery timeproduct quality received display issue word return replacement update jan month support based experience request buy seller rip money purchased value money look retail options amazon fullfillment policy vendor strikehrough comment added amzn feedback https www amazon gp help seller glance html ref ppx od dt sellerprofile ie utf isamazonfulfilled marketplaceseller orderid seller ev fczwl exited piece month usage found backup bad charge drain bedtime internet watching videos difficulties module nice compact night mode nice potrait mode takes process result fantastic days usage found heavy gamer camera calls smooth hz bit slippery hand protect hand fingerprint unlock unlock fast iphone otherwise speed camera equals iphone edited week usage found optimized getting solid nice light weight size comfortable handle ideal searching excellent hope won regret browser support html video light excellent design camera superb overall experience flawless competetive imported brilliant size little xl range phones speaker mind boggling camera world buy doubts recieved warranty card rd using amazing camera quality easy worth money coz reasons form factor age epidemic inch slabs messiah example phones imo inches perfect size smartphone keeping ur pocket operating hand camera guesses photo processing smartphones clicks pics little noise especially love night mode fan mode reasons switch previous yr yeah lasts dont worry carrying power banks play heavy games run faster delivery timeproduct quality received display issue word return replacement update jan month support based experience request buy seller rip money purchased value money look retail options amazon fullfillment policy vendor strikehrough comment added amzn feedback https www amazon gp help seller glance html ref ppx od dt sellerprofile ie utf isamazonfulfilled marketplaceseller orderid seller ev fczwl exited piece month usage found backup bad charge drain bedtime internet watching videos difficulties module nice compact night mode nice potrait mode takes process result fantastic days usage found heavy gamer camera calls smooth hz bit slippery hand protect hand fingerprint unlock unlock fast iphone otherwise speed camera equals iphone edited week usage found optimized getting solid nice light weight size comfortable handle ideal searching excellent hope won regret browser support html video light excellent design camera superb overall experience flawless competetive imported brilliant size little xl range phones speaker mind boggling camera world buy doubts recieved warranty card rd using amazing camera quality easy worth money coz reasons form factor age epidemic inch slabs messiah example phones imo inches perfect size smartphone keeping ur pocket operating hand camera guesses photo processing smartphones clicks pics little noise especially love night mode fan mode reasons switch previous yr yeah lasts dont worry carrying power banks play heavy games run faster delivery timeproduct quality received display issue word return replacement update jan month support based experience request buy seller rip money purchased value money look retail options amazon fullfillment policy vendor strikehrough comment added amzn feedback https www amazon gp help seller glance html ref ppx od dt sellerprofile ie utf isamazonfulfilled marketplaceseller orderid seller ev fczwl exited piece month usage found backup bad charge drain bedtime internet watching videos difficulties module nice compact night mode nice potrait mode takes process result fantastic days usage found heavy gamer camera calls smooth hz bit slippery hand protect hand fingerprint unlock unlock fast iphone otherwise speed camera equals iphone edited week usage found optimized getting solid nice light weight size comfortable handle ideal searching excellent hope won regret "

nltk_tokens = nltk.word_tokenize(word_data)  	

print(list(nltk.bigrams(nltk_tokens)))

nltk_tokens = [w for w in nltk_tokens if not w in stopwords]
bigram_cloud = " ".join(nltk_tokens)
#WORDCLOUD

wordcloud_ip = WordCloud(
                      background_color='White',  repeat=False,
                      width=2000,
                      height=1500
                     ).generate(bigram_cloud)

plt.imshow(wordcloud_ip)

########################################################################

#PROBLEM STATEMENT:-2

#Extract reviews for any movie from IMDB and perform sentiment analysis
#Choose any other website on the internet and do some research on how to extract text and perform sentiment analysis


import requests
from bs4 import BeautifulSoup as bs
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud 


movie_rating=[]

for i in range(1,5):
    ip=[]
    url="https://www.imdb.com/title/tt1954470/reviews?ref_=tt_urv"
    response = requests.get(url)
    soup = bs(response.content,"html.parser") 
    reviews = soup.find_all("div",attrs={"class","review-container"})  
    for i in range(len(reviews)):
        ip.append(reviews[i].text) 
    movie_rating=movie_rating+ip  

with open("movie_review.txt","w",encoding='utf8') as output:
    output.write(str(movie_rating))
   
# Joinining all the reviews into single paragraph 
ip_rev_string = " ".join(movie_rating)

# from nltk.corpus import stopwords
import nltk

# Removing unwanted symbols incase if exists
ip_rev_string = re.sub("[^A-Za-z" "]+"," ", ip_rev_string).lower()
ip_rev_string = re.sub("[0-9" "]+"," ", ip_rev_string)

# words that contained in iphone XR reviews
ip_reviews_words = ip_rev_string.split(" ")

#TFIDF
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(ip_reviews_words, use_idf=True,ngram_range=(1, 3))
X = vectorizer.fit_transform(ip_reviews_words)

#additional stopword removing from a stopword textfile
with open("C:\\Users\\prash\\Desktop\\ASIGNMENT\\TEXT MINING\\stopwords.txt","r") as sw:
    stopwords = sw.read()
    
stopwords=stopwords.split("\n")
stopwords.extend(["movie","film","hindi","time","song","sign","such","dance","review","helpful"])

ip_reviews_words = [w for w in ip_reviews_words if not w in stopwords]

# Joinining all the reviews into single paragraph 
ip_rev_string = " ".join(ip_reviews_words)

# WordCloud can be performed on the string inputs.
# Corpus level word cloud

wordcloud_ip = WordCloud(
                      background_color='White',
                      width=1800,
                      height=1400
                     ).generate(ip_rev_string)

plt.imshow(wordcloud_ip)

###################################################################
































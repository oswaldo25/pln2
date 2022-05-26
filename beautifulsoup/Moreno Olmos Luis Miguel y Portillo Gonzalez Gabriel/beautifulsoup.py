# -*- coding: utf-8 -*-
"""
Created on Tue May 24 11:25:45 2022

@author: luis_ 2da edicion
"""

import urllib.request
from bs4 import BeautifulSoup
import nltk
from nltk import word_tokenize

url = "https://www.sas.com/es_ar/insights/analytics/what-is-natural-language-processing-nlp.html"

html = urllib.request.urlopen(url)

htmlParse = BeautifulSoup(html, 'html.parser')

text= htmlParse.get_text()
tokens= nltk.word_tokenize(text)
title = htmlParse.title

print("Title: ",title,"\n")
print("Type:",type(tokens),"\n")
print("Total tokens: ",len(tokens),"\n")
print(tokens[:15])

text = nltk.Text(tokens)
text.findall("<PLN>(<.*>)")
text.concordance("PLN")

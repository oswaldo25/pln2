# -*- coding: utf-8 -*-
"""
Created on Tue May 24 11:25:45 2022

@author: luis_
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

htmlwords = ['https', 'http', 'display', 'button', 'hover',
             'color', 'background', 'height', 'none', 'target',
             'WebPage', 'reload', 'fieldset', 'padding', 'input',
            'select', 'textarea', 'html', 'form', 'cursor',
            'overflow', 'format', 'italic', 'normal', 'truetype',
            'before', 'name', 'label', 'float', 'title', 'arial', 'type',
            'block', 'audio', 'inline', 'canvas', 'margin', 'serif', 'menu',
            'woff', 'content', 'fixed', 'media', 'position', 'relative', 'hidden',
            'width', 'clear', 'body', 'standard', 'expandable', 'helvetica',
            'fullwidth', 'embed', 'expandfull', 'fullstandardwidth', 'left', 'middle',
            'iframe', 'rgba', 'selected', 'scroll', 'opacity',
            'center', 'false', 'right']

words = [w for w in tokens if w.isalpha() and len(w) > 4 and w.lower() not in htmlwords]

text2 = nltk.Text(words)

freqdist = nltk.probability.FreqDist(text2)
freqdist.plot(20)
freqdist.plot(20, cumulative=True)


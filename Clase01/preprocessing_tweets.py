#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
import re
import nltk
import spacy
import string
from tqdm.auto import tqdm
import csv
from emo_unicode import EMOTICONS, UNICODE_EMO  
from nltk.corpus import stopwords
import codecs
import emoji
import codecs
     

def tolower(text):
    return text.str.lower()


def remove_mentions_urls(text):
    text = re.sub(r"(?:\@|https?\://)\S+", "", text)
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)  

def remove_hts(text):
    text = re.sub("#[A-Za-z_Ññ_0-9_]+"," ", text)
    return ' '.join(text.split())

def convert_emoticons(text):
    for emot in EMOTICONS:
        text = re.sub(u'('+emot+')', " "+"_".join(EMOTICONS[emot].replace(",","").split())+" ", text)
    return ' '.join(text.split())


def convert_emojis(text):
    text = emoji.demojize(text, delimiters=(" ", " "))
    return ' '.join(text.split())

def remove_nonascii(text):
    return ' '.join(re.sub(r'[^\w\s]',' ',text).split())

def remove_punctuation(text):
    PUNCT_TO_REMOVE = string.punctuation
    PUNCT_TO_REMOVE = PUNCT_TO_REMOVE.replace("_","")
    PUNCT_TO_REMOVE = PUNCT_TO_REMOVE+'“'+'”'+'¿'+'¡'+'►'+'´'
    """custom function to remove the punctuation"""
    translator = str.maketrans(PUNCT_TO_REMOVE, ' '*len(PUNCT_TO_REMOVE))
    text = text.translate(translator)
    return ' '.join(text.split())

def remove_accents(text):
    return text.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')

def create_stopwords():
    import codecs
    list_stop = []
    with codecs.open('stopwords_es.txt', 'r', encoding='latin1', errors='ignore') as fp:
        for line in fp:
            list_stop.append(line.strip())  
    sws = ",".join(stopwords.words('spanish'))
    list_stop = ','.join(list_stop).replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    sws = sws.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    sws = set(sws.strip().split(",")).union(set(list_stop.split(","))) 
    return sws

def remove_stopwords(text, stopwords):
    return " ".join([word for word in str(text).split() if word not in stopwords])


def remove_numbers(text):
   text = re.sub(r'[0-9]', " ",text)
   return ' '.join(text.split())

def remove_dots(text):
    text = text.replace("…"," ")
    return ' '.join(text.split())

    
    

        

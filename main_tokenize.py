from __future__ import division
import json
import pandas as pd
import numpy as np
import requests
import nltk
import string
import re
import os
from os import path
from time import sleep
from collections import Counter
from nltk.tokenize import TweetTokenizer
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import twitter_samples
from random import shuffle

def tokenizeTweets(tweetList):
    useless_ones = nltk.corpus.stopwords.words("english") + list(string.punctuation)
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=False, reduce_len=False)
    retTweetList = []
    for tweet in tweetList:
        wordlist = [word for word in tokenizer.tokenize(tweet) if word not in useless_ones]
        retTweetList.append(wordlist)
    return retTweetList

def stemTweets(tweetList):
    sno = nltk.stem.SnowballStemmer("english")
    retTweetList = []
    for words in tweetList:
        stemmed_words = [sno.stem(word) for word in words]
        retTweetList.append(stemmed_words)
    return retTweetList

def main(twtInfo:object):
    clean_data_tweets = pd.read_json(twtInfo, orient="records", lines=True)
    nltk.download("stopwords")
    nltk.download("punkt")
    data_tc_tweets = tokenizeTweets(clean_data_tweets)
    data_tcs_tweets = stemTweets(data_tc_tweets)
    return pd.Series(data_tcs_tweets).to_json(orient="records")

dat = main("C:/Users/Matt/Documents/GitHub/twitter-sentiment-analysis/test_clean_out.json")
with open("test_token_out.json", "w+") as out:
    out.write(dat)
import json
import pandas as pd
import string
import nltk
from nltk.tokenize import TweetTokenizer

def tokenizeTweets(tweetList):
    useless_ones = nltk.corpus.stopwords.words("english") + list(string.punctuation)
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=False, reduce_len=False)
    retTweetList = []
    for tweet in tweetList:
        wordlist = [word for word in tokenizer.tokenize(tweet) if word not in useless_ones]
        retTweetList.append(wordlist)
    return retTweetList

def tokenizeTweet(tweet):
    useless_ones = nltk.corpus.stopwords.words("english") + list(string.punctuation)
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=False, reduce_len=False)
    wordlist = [word for word in tokenizer.tokenize(tweet) if word not in useless_ones]
    return wordlist

def main(twtInfo:object):
    clean_data_tweets = pd.read_json(twtInfo, orient="records")
    nltk.download("stopwords")
    nltk.download("punkt")
    tweets = clean_data_tweets["text"]
    data_id = clean_data_tweets["id"]
    data_tc_tweets = []
    for tweet in tweets:
        data_tc_tweets.append(tokenizeTweet(tweet))
    ret = []
    for i in range(len(data_tc_tweets)):
        ret.append({})
        ret[i]["text"] = data_tc_tweets[i]
        ret[i]["id"] = data_id[i]
    return pd.Series(ret).to_json(orient="records")

<<<<<<< HEAD:main_tokenize.py
dat = main("test_clean_out.json")
with open("test_token_out.json", "w+") as out:
    out.write(dat)
=======
>>>>>>> 1e17e98119a5a26e4749b372a47c4504bc3ed9d0:Tweet_Tokenize.py

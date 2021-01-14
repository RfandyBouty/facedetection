import twitter

twitter_api = twitter.Api(consumer_key="C8oKuw6NgpGz4UkJP8xX6JaPg",
consumer_secret='cM9KR2NrI9FmA1AdHyaRDRAbVrr6aSLvscYS1UadSKUVJxEc0O', access_token_key='1227814781446279169-ghBujWKQhoQTI2evd6p3pmlP2QPPZh',access_token_secret='KcYz65bOqznM2wMcj4PjXPyJeNQiZCWU42C9XMRBK3wRL')

def buildTestSet(search_keyword):
    try:
        tweets_fetched = twitter_api.GetSearch(search_keyword, count = 100)
        print("fetched " + str(len(tweets_fetched)) + " tweets for the term " + search_keyword)
        return [{"text":status.text, "label":None} for status in tweets_fetched]
    except:
        print("Gagal")
        return None
    
search_term = input("Keyword: ")
testDataSet = buildTestSet(search_term)

print(testDataSet[0:4])

# training data set

def buildTrainingSet(corpusFile, tweetDataFile):
    import csv
    import time

    corpus=[]

    rate_limit=180
    sleep_time=900/180

    trainingDataSet=[]

    for tweet in corpus:
        try:
            status = twitter_api.GetStatus(tweet["tweet_id"])
            print("Tweet fetched" + status.text)
            tweet["text"] = status.text
            trainingDataSet.append(tweet)
            time.sleep(sleep_time)
        except:
            continue
    
    with open(tweetDataFile, 'wb') as csvfile:
        linewriter = csv.writer(csvfile,delimiter=',', qoutechar="\"")
        for tweet in trainingDataSet:
            try:
                linewriter.writerow([tweet["tweet_id"], tweet["text"], tweet["label"], tweet["topic"]])
            except Exception as e:
                print(e)
    return trainingDataSet      
    
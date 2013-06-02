import random
import twitter
import data.bert.models as bert

def tweet_random():
    num = random.randint(0, 100)
    if num == 50:
        txt = bert.get_random_bert_speak(3)        
        if txt is not None and txt != '':
            txt = (txt[:130] + '..') if len(txt) > 139 else data
            #t = twitter.Twitter(auth=twitter.OAuth())
            #t.statuses.update(status=txt)            

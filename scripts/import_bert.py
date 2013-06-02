import sys
sys.path.append('./')

import transaction
import csv
import data.common as common
import data.bert.models as models

common.init('sqlite:///bert.sqlite')

def add_speak(text, pos):
    return {'text':text, 'pos':pos}

def do_row(r, i):    
    print i
    print r[i]    
    bert = models.Bert()
    bert.text = r[i]
    bert.pos = i
    models.add_bert_speak(bert)        

with transaction.manager:
    with open('external_data/BrisBertCopy - dataset.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            for i in range(6):
                do_row(row, i)

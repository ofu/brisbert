import sys
sys.path.append('./')

import transaction
import data.common as common
import data.bert.models as models

common.init('sqlite:///bert.sqlite')

def add_speak(text, pos):
    return {'text':text, 'pos':pos}

bert_speak = [
    add_speak('Do not talk to me about {{search_text}}.', 0),
    add_speak('I love {{search_text}}', 0),
    add_speak('My dad used to go wild about {{search_text}}.', 0),
    add_speak('{{search_text}} makes me laugh.', 0),
    add_speak('Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 1),
    add_speak('cursus eu nunc.', 1),
    add_speak('Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Cura', 1),
    add_speak('Aenean euismod tellus est.', 1),
    add_speak('Morbi at erat leo, consectetur faucibus diam', 1),
    add_speak('I like frogs.', 1),
    add_speak('Did I tell you about the time?', 1),
    add_speak('Go on, go an look at {{keyword1}} instead', 2),
    add_speak('I am tired about hearing about {{search_text}}, let me tell you about {{keyword1}}!', 2),
]

with transaction.manager:
    for copy in bert_speak:
        bert = models.Bert()
        bert.text = copy['text']
        bert.pos = copy['pos']
        models.add_bert_speak(bert)

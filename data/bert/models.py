import random
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode
import data.common as common

format_year = 0   
format_short = 1
format_long = 2  
format_random = 3

class Bert(common.Base):
    __tablename__ = 'bert_speaks'
    id = Column(Integer, primary_key=True)    
    text = Column(Unicode(256))  
    pos = Column(Integer)     

def add_bert_speak(bert):
    """
    Used initially just to import data from csv into sqlite
    """
    session = common.DBSession()
    session.add(bert)

def get_random_bert_speak(pos):
    if pos == format_year:
        return _get_random(0)
    elif pos == format_short:
        return _get_random(1)
    elif pos == format_long:
        return '%s %s %s' % (_get_random(2), _get_random(3), _get_random(4))
    elif pos == format_random:
        return _get_random(5)

def _get_random(pos):
    session = common.DBSession()
    query = session.query(Bert)
    query = query.filter_by(pos=pos)
    results = query.all()    
    offset = random.randint(0, len(results) - 1)
    result = results[offset]
    if result is None:
        result = Bert()
        result.pos = pos
    if result.text == '':
        result.text = 'Erm, well, what were we talking about again?'        
    return result.text


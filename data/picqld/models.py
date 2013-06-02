from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode
import data.common as common


class Picture(common.Base):
    __tablename__ = 'picqld_pictures'
    id = Column(Integer, primary_key=True)    
    title = Column(Unicode(128))  
    description = Column(Unicode(256))
    subjects = Column(Unicode(128))
    year = Column(Integer)
    small_url = Column(Unicode(128))
    large_url = Column(Unicode(128))


def add_picture(picture):
    """
    Used initially just to import data from csv into sqlite
    """
    session = common.DBSession()
    session.add(picture)

    
def get_item_by_id(value):
    session = common.DBSession()
    query = session.query(Picture)
    query = query.filter_by(id=value)
    return query.first()    

    
def get_items_by_keywords(value, num):
    session = common.DBSession()
    query = session.query(Picture)
    query = query.filter(Picture.description.like('%' + value + '%'))
    query = query.limit(num)
    return query.all()

    
def get_items_by_date(value, num):
    session = common.DBSession()
    query = session.query(Picture)
    query = query.filter_by(Picture.year == int(value))
    query = query.limit(num)
    return query.all()

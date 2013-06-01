from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import Unicode
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
import data.common as common


class Collection(common.Base):
    __tablename__ = 'myouseum150_collection'
    id = Column(Integer, primary_key=True)    
    title = Column(Unicode(64))
    description = Column(Unicode(64))
    date = Column(DateTime)
    year = Column(Integer)
    items = relationship("CollectionItem", backref="collection", cascade="all,delete")


class CollectionItem(common.Base):
    __tablename__ = 'myouseum150_collections_item'
    id = Column(Integer, primary_key=True)
    photo_id = Column(Integer)    
    object_name = Column(Unicode(64))
    scientific_name = Column(Unicode(64))
    story = Column(Unicode(1024))
    vernon_id = Column(Unicode(32))
    qm_filename = Column(Unicode(64))
    credit = Column(Unicode(64))
    comment = Column(Unicode(256))
    collections_id = Column(Integer, ForeignKey(Collection.id), nullable=False)    


class Photo(common.Base):
    __tablename__ = 'myouseum150_photo'
    id = Column(Integer, primary_key=True)
    object_name = Column(Unicode(64))
    scientific_name = Column(Unicode(64))
    story = Column(Unicode(1024))
    vernon_id = Column(Unicode(32))
    qm_filename = Column(Unicode(64))
    credit = Column(Unicode(64))

def add_collection(collection):
    """
    Used initially just to import data from csv into sqlite
    """
    session = common.DBSession()
    c = session.query(Collection).filter_by(id=collection.id).first()
    if c is None:
        session.add(collection)
        session.flush()
        c = collection
    return c

def add_collection_item(collection, collection_item):
    """
    Used initially just to import data from csv into sqlite
    """
    session = common.DBSession()
    collection_item.collections_id = collection.id
    session.add(collection_item)

def add_photo(photo):
    """
    Used initially just to import data from csv into sqlite
    """
    session = common.DBSession()
    session.add(photo)

def get_item_by_id(value):
    session = common.DBSession()
    query = session.query(CollectionItem)
    query.filter_by(id=value)
    return query.first()    

def get_items_by_keywords(value, num):
    session = common.DBSession()
    query = session.query(CollectionItem)
    query = query.filter(CollectionItem.story.like('%' + value + '%'))
    query = query.limit(num)
    return query.all()

def get_items_by_date(value, num):
    session = common.DBSession()
    query = session.query(Collection)
    query = query.filter_by(Collection.year == int(value))
    query = query.limit(num)
    return query.all()

def get_photo_by_id(value):
    session = common.DBSession()
    query = session.query(Photo)
    query.filter_by(id=value)
    return query.first()    

def get_photos_by_keywords(value, num):
    session = common.DBSession()
    query = session.query(Photo)
    query = query.filter(Photo.story.like('%' + value + '%'))
    query = query.limit(num)
    return query.all()


from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import Unicode
from sqlalchemy import Boolean
from sqlalchemy import Binary
from sqlalchemy import PickleType
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from datetime import datetime
import data.common as common


class Collection(common.Base):
    __tablename__ = 'myouseum150_collection'
    id = Column(Integer, primary_key=True)    
    title = Column(Unicode(64))
    description = Column(Unicode(64))
    date = Column(DateTime)
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

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

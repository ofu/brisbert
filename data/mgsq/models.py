from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode
import data.common as common


class Museum(common.Base):
    __tablename__ = 'mgsq_museum'
    id = Column(Integer, primary_key=True)    
    organisation_name = Column(Unicode(64))  
    postal_address_1 = Column(Unicode(64))    
    postal_address_2 = Column(Unicode(64))    
    town = Column(Unicode(64))      
    state = Column(Unicode(64))     
    pcode = Column(Unicode(64))    
    physical_address_1 = Column(Unicode(64))        
    physical_address_2 = Column(Unicode(64))        
    physical_Town = Column(Unicode(64))        
    physical_state = Column(Unicode(64))       
    physical_pcode = Column(Unicode(64))    
    phone = Column(Unicode(64))          
    email = Column(Unicode(64))          
    website = Column(Unicode(64))        
    opening_times = Column(Unicode(64))           
    admission_cost = Column(Unicode(64))          
    wheelchair_access = Column(Unicode(64))           
    toilets = Column(Unicode(64))        
    guided_tours = Column(Unicode(64))        
    merchandise_for_sale = Column(Unicode(64))
    cafe = Column(Unicode(64))           
    collection_specification = Column(Unicode(64))       


def add_museum(museum):
    """
    Used initially just to import data from csv into sqlite
    """
    session = common.DBSession()
    session.add(museum)

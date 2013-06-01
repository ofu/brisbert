import dummy
import myouseum
import data.common as common

""" Engine list used by the apibert. Objects in the list can be either class 
instances, or modules
"""
engine_list_ = { 
    'myouseumi': myouseum.CollectionItemEngine(),
    'myouseump': myouseum.CollectionPhotoEngine(),
}

""" Engine descriptions, used by the front end to attribute 
"""
engine_desc_ = {
    'myouseumi': 'Queensland Museum Information, MYOUSEUM150',
    'myouseump': 'Queensland Museum Information, MYOUSEUM150',
}

common.init('sqlite:///bert.sqlite')    
    
def get_engines():
    """ Returns a map of database names to their corresponding engines
    """
    return engine_list_


def engine_desc(engine_name):
    """ Returns a description of the database engine, or '' if no description 
    can be found for the engine_name
    """
    return '' if engine_name not in engine_desc_ else engine_desc_[engine_name]
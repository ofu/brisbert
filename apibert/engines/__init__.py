import dummy
import myouseum

""" Engine list used by the apibert. Objects in the list can be either class 
instances, or modules
"""
engine_list_ = { 
    'myouseumi': myouseum.CollectionItemEngine(),
}

""" Engine descriptions, used by the front end to attribute 
"""
engine_desc_ = {
    'myouseumi': 'Queensland Museum Information, stuff, things, and more staff attributing all stuff to things',
}
    
    
def get_engines():
    """ Returns a map of database names to their corresponding engines
    """
    return engine_list_


def engine_desc(engine_name):
    """ Returns a description of the database engine, or '' if no description 
    can be found for the engine_name
    """
    return '' if engine_name not in engine_desc_ else engine_desc_[engine_name]
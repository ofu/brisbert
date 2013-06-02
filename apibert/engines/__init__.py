import dummy
import myouseum
import picqld
import trove
import data.common as common

""" Engine list used by the apibert. Objects in the list can be either class 
instances, or modules
"""
engine_list_ = { 
    'myouseumi': myouseum.CollectionItemEngine(),
    'myouseump': myouseum.CollectionPhotoEngine(),
    'picqld': picqld.PictureQueenslandEngine(),
    'trove': trove.TroveBaseEngine()
}

""" Engine descriptions, used by the front end to attribute 
"""
engine_desc_ = {
    'myouseumi': 'Queensland Museum Information, MYOUSEUM150',
    'myouseump': 'Queensland Museum Information, MYOUSEUM150',
    'picqld': 'Pictures Queensland, 40 000 out of copyright photographs from the photograph collection of the State Library of Queensland. People and places from across Queensland across time',
    'trove': 'Trove Stuff'
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
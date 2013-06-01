import dummy

""" Engine list used by the apibert. Objects in the list can be either class 
instances, or modules
"""
engine_list_ = { 'dummy': dummy.Dummy() }

def get_engines():
    return engine_list_
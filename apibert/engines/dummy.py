
""" Default dictionary returned by the dummy class, only the database and id 
fields are required, all the rest are optional
"""
default_ = { 'id': 100, 
             'keyword': 'pineapple onion belt',
             'date': '10-12-2009',
             'text': 'Crazy optional text',
             'url' : '/static/dummy/01.jpg' }

class Dummy(object):
    """ Dummy engine class, returns a dict object for certain methods called
    """

    def keyword(self, value, num, request):
        """ Returns at most num dict objects, as an iterable, with keyword as a 
        keyword in the dict.
        """
        retval = dict(default_)
        retval['keyword'] = value
        return [ retval ]

    def date(self, value, num, request):
        """ Returns at most num dict objects, as an iterable, with all dict 
        objects matching the date passed
        """
        retval = dict(default_)
        retval['date'] = value
        return [ retval ]

    def id(self, value, num, request):
        """ Returns at most 1 dict objects, as an iterable, specified by its id 
        of value
        """
        retval = dict(default_)
        retval['id'] = value
        return [ retval ]

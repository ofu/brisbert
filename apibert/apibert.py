import bottle
import engines
import random

""" Set of keys useable by the rest api
"""
engines_key_set_ = {'keyword', 'date'}

""" Rqeuired params for the data_view
"""
data_required_params_ = {'value', 'num'}


def _get_key(engine, name, key, value, num, request):
    """ Returns the query for the specified engine for the specified key. Also
    adds the database name to the returned dictionary
    """
    retval = getattr(engine, key)(value, num, request)
    for obj in retval:
        obj.setdefault('database', name)
        
    return retval


@bottle.get('/brisbert/<search_key>')
def data_route(search_key):
    """ Returns for json data based on a search key, and parameters passed in 
    the GET request. The following GET parameters are parsed:
    
    value: value of the key to search for <required>
    num: number of values to return <required>
    
    """
    if search_key not in engines_key_set_:
        return bottle.abort(404, 'Search key unknown')
        
    for required in data_required_params_: 
        if required not in bottle.request.query:
            return bottle.abort(400, "Missing param: " + required)
    
    engine_list = engines.get_engines()
    
    objs = []
    for engine in engine_list.iteritems():
        objs.extend(_get_key(engine[1], engine[0], search_key, 
                             bottle.request.query['value'], 
                             int(bottle.request.query['num']), bottle.request))
    random.shuffle(objs)
    return { 'objects': objs[:int(bottle.request.query['num'])] }


@bottle.get('/brisbert/<database>/<id>')
def database_id_route(database, id):
    """ Returns a specific item based on an id
    """
    searches = engines.get_engines()
    if database not in searches:
        return bottle.abort(400, 'Bad database: ' + database)
        
    return _get_key(searches[database], database, 'id', id, 1, request)


@bottle.get('/static/<filename:path>')
def static_route(filename):
    """Route for our static resources
    """
    return  bottle.static_file(filename, root='./static/')
                                            
if __name__ == '__main__':
    bottle.run(host='localhost', port=8080, debug=True)

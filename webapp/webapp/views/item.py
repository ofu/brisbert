from pyramid.view import view_config
import requests

@view_config(route_name='item', renderer='templates/home/item.jinja2')
def home(request):

    dbname = request.matchdict['db']
    idval = request.matchdict['id']

    url = 'http://127.0.0.1:8080/brisbert/' + dbname + '/' + idval
    r = requests.get(url)
    search_results = r.json()
    print 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    print search_results
    return {
        'result': search_results['objects'][0]
    }

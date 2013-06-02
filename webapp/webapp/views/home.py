import random
import requests
from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/home/home.jinja2')
def home(request):
    search_results = []
    twitter_feed = True
    search_query = None
    if 'search_query' in request.GET:
        search_query = request.GET['search_query']        
    if 'search_query' in request.POST:
        search_query = request.POST['search_query']
    if search_query is not None:
        twitter_feed = False                
        url = 'http://127.0.0.1:8080/brisbert/keyword'
        r = requests.get(url, params={'value':search_query, 'num':'20'})
        search_results = r.json()
    else:
        search_query = 'Brisbane'

    return {
        'subject': "robots",
        'search_results': search_results,
        'twitter_feed': twitter_feed,
        'get_kw': _get_kw,
        'search_query': search_query,
    }

def _get_kw(keywords):
    if len(keywords) > 0:
        index = random.randint(0, len(keywords) - 1)
        return keywords[index]
    return 'Brisbane'

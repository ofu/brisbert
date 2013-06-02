from pyramid.view import view_config
import requests

@view_config(route_name='home', renderer='templates/home/home.jinja2')
def home(request):
    search_results = []
    twitter_feed = True
    if 'search_query' in request.POST:
        twitter_feed = False
        search_query = request.POST['search_query']        
        url = 'http://127.0.0.1:8080/brisbert/keyword'
        r = requests.get(url, params={'value':search_query, 'num':'20'})
        search_results = r.json()

    return {
        'subject': "robots",
        'search_results': search_results,
        'twitter_feed': twitter_feed,
        'get_kw': _get_kw
    }

def _get_kw(keywords):
    if len(keywords) > 0:
        return keywords[0]
    return 'Brisbane'
    
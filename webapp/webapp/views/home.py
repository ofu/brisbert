from pyramid.view import view_config
import requests

@view_config(route_name='home', renderer='templates/home/home.jinja2')
def home(request):
    year = 2012
    url = 'http://127.0.0.1:8080/brisbert/keyword'
    r = requests.get(url, params={'value':'saurus', 'num':'10'})
    search_results = r.json()
    print search_results
    return {
        'subject': "robots",
        'year': year,
        'search_results': search_results
    }
